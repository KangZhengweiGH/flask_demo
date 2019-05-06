from flask import Flask
from extend import db
from celery import Celery
from celeryconfig import broker_url


celery = Celery(__name__, broker_url=broker_url)


def creat_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)
    register_celery(app)
    db.init_app(app)
    from account import account as account_buleprint
    from book import book as book_buleprint
    from main import main as main_buleprint
    from test.views import test as test_buleprint
    app.register_blueprint(account_buleprint, url_prefix='/account')
    app.register_blueprint(book_buleprint, url_prefix='/book')
    app.register_blueprint(test_buleprint, url_prefix='/test')
    app.register_blueprint(main_buleprint)
    return app


def register_celery(app):
    celery.config_from_object('celeryconfig')

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = ContextTask
