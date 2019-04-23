from flask import Flask
from extend import db
# from flask_bootstrap import Bootstrap


def creat_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)
    # bootstrap = Bootstrap(app)
    db.init_app(app)
    from account.views import account as account_buleprint
    from book.views import book as book_buleprint
    from main.views import main as main_buleprint
    # from admin.views import admin as admin_buleprint
    app.register_blueprint(account_buleprint, url_prefix='/account')
    app.register_blueprint(book_buleprint, url_prefix='/book')
    # app.register_blueprint(admin_buleprint, url_prefix='/admin')
    app.register_blueprint(main_buleprint)

    return app
