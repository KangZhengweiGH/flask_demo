from flask import Flask
import config
from extend import db


def creat_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    from account.views import account
    app.register_blueprint(account, url_prefix='/account')

    return app
