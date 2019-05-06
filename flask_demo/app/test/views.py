from .form import MyForm
from flask import redirect, render_template, Blueprint, request, url_for

test = Blueprint('test', __name__, template_folder='templates/test', static_folder='static')


@test.route('/success/')
def success():
    return render_template('test/success.html')


@test.route('/submit/', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect(url_for('test.success'))
    return render_template('test/submit.html', form=form)

