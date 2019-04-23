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

book = Blueprint('book', __name__, template_folder='templates', static_folder='static')

# @book.route('/')