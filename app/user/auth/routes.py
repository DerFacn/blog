from flask import request, render_template
from .utils import generate_hash
from .forms import AuthForm


def signup():
    form = AuthForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form.get('username', None)
            password = request.form.get('password', None)
            return f"{username} | {generate_hash(password)}"
    return render_template('auth/signup.html', form=form)


def login():
    if request.method == 'POST':
        pass
    return render_template('auth/login.html')


def logout():
    pass
