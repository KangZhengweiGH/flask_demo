# encoding: utf-8
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from extend import db
from __init__ import creat_app
import config

from modles import User, Book, Chapter, Category

app = creat_app(config)
manager = Manager(app)

# 绑定app和db
migrate = Migrate(app, db)
# 把MigrateCommand命令添加到manager中
manager.add_command('db', MigrateCommand)
# init migrate upgrade


if __name__ == "__main__":
    manager.run()
