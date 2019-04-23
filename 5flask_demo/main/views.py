# encoding: utf-8
from flask import (session,
                   render_template,
                   url_for,
                   redirect,
                   request,
                   jsonify)

from extend import db
from modles import User
from flask import Blueprint

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
