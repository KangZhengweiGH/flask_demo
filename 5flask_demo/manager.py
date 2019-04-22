# encoding: utf-8
from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from extend import db
from . import creat_app

from modles import User, Book, Chapter, Category

app = creat_app()

manager = Manager(app)

# 绑定app和db
migrate = Migrate(app, db)
# 把MigrateCommand命令添加到manager中
manager.add_command('db', MigrateCommand)
# init migrate upgrade


@app.context_processor
def user_status():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}


if __name__ == "__main__":
    manager.run()
