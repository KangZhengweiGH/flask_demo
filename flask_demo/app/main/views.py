# encoding: utf-8
from flask import session, render_template, Blueprint
import time
from app.modles import User
from app.main.task import long
main = Blueprint('main', __name__, template_folder='templates', static_folder='static')


@main.route('/')
def index():
    return render_template('index.html')


@main.context_processor
def user_status():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}


@main.route('/long')
def long_io():
    long.delay()
    print('I have waited for 10s')
    return 'I have waited for 10s'
