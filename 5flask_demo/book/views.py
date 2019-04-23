# encoding: utf-8
from flask import (session,
                   render_template,
                   request,
                   jsonify)
import json
from extend import db
from modles import Book, Category
from flask import Blueprint

book = Blueprint('book', __name__, template_folder='templates', static_folder='static')


@book.route('/', methods=['GET', 'POST'])
def add_book():
    if request.method == 'GET':
        return render_template('addbook.html')
    name = request.form.get('bookname')
    need_vip = request.form.get('need_vip')
    introduce = request.form.get('introduce')
    book_image = request.form.get('book_image')
    category_id = request.form.get('category_id')

    if name:
        bookitem = Book(name=name, introduce=introduce, book_image=book_image, need_vip=need_vip,  category_id=category_id)
        db.session.add(bookitem)
        db.session.commit()
        return "okokoko"
    return '名字不能为空aaaaaaa'


@book.route('/addcategory', methods=['GET', 'POST'])
def add_category():
    if request.method == "GET":
        return render_template('category.html')
    name = request.form.get('category_name')
    father = request.form.get('fatherc_id')
    print(name)
    if name:
        categoryitem = Category(name=name, fatherc_id=father)
        db.session.add(categoryitem)
        db.session.commit()
        return '''<a href="/book/addcategory">返回</a>'''
    return "类名不能为空bbbbbbbb"


@book.route('/bkindex')
def bookindex():
    books = Book.query.all()
    print(books)
    books_data = {}
    for item in books:
        books_data[item.id] = [item.name, item.introduce]
    return jsonify(books_data)


@book.route('/cgindex')
def categoryindex():
    categorys = Category.query.all()
    categorys_data = {}
    for item in categorys:
        categorys_data[item.id] = [item.name]
    return jsonify(categorys_data)
