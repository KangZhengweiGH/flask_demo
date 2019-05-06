# encoding: utf-8
from flask import session, render_template, Blueprint
import time
from __init__ import celery
from modles import User

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


@celery.task
def long():
    time.sleep(10)


@main.route('/long')
def long_io():
    long()
    return 'I have sleeped 10s'

