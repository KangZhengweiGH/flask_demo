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


account = Blueprint('account', __name__, template_folder='templates', static_folder='static')


@account.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    login_name = request.form.get('user')
    passwd = request.form.get('password')
    # login_name # 本打算处理不同方式登陆暂不处理，一律按手机
    user = User.query.filter(User.telnumber == login_name, User.password == passwd).first()
    if user:
        session['user_id'] = user.id
        session.permanent = True
        return redirect(url_for('main.index'))
    return render_template('login.html', error3='账号或密码错误')


@account.route('/logout')
def logout():
    # session.pop('user_id')
    # del session('user_id')
    session.clear()
    return redirect(url_for('main.index'))


@account.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')

    telnumber = request.form.get('telnumber')
    passwd1 = request.form.get('passwd1')
    passwd2 = request.form.get('passwd2')
    tel = User.query.filter(User.telnumber == telnumber).first()
    error = None
    if tel:
        error = "该号码已注册"
        return render_template('regist.html', error1=error)

    elif passwd1 != passwd2:
        error = "密码不一致"
        return render_template('regist.html', error2=error)

    else:
        user = User(telnumber=telnumber, password=passwd1)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('account.login'))


# todo此处要加是否登陆装饰器,额这里不确定
@account.route('/createvip/<user_id>', methods=['GET'])
def create_vip(user_id):
    user = User.query.filter(User.id == user_id).first()
    print(user)
    if user:
        user.vip = True
        db.session.commit()

    return redirect(url_for('account.userinfo', user_id=user_id))


# todo此处要加是否登陆装饰器
@account.route('/userinfo/<user_id>')
def userinfo(user_id):
    user = User.query.filter(User.id == user_id).first()
    if user:
        data = {
            'id': user.id,
            'name': user.name,
            'passwd': user.password,
            'telnumber': user.telnumber,
            'vip': user.vip,
            'logintime': user.logintime

        }
        return jsonify(data)

    return redirect(url_for('main.index'))
