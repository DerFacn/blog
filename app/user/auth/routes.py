from flask import request, render_template, flash, make_response, redirect, url_for, g
from .utils import generate_hash, check_hash, create_token
from .forms import SignupForm, LoginForm
from app.models import User
from app.db import session
from sqlalchemy.exc import IntegrityError
from uuid import uuid4
from .verification import send_message, verify


def signup():
    if g.user:
        return redirect('/')

    form = SignupForm()
    if request.method == 'POST':
        if form.validate_on_submit():

            username = request.form.get('username', None)
            password = request.form.get('password', None)
            email = request.form.get('email')
            identity = str(uuid4())

            new_user = User(uuid=identity, username=username, email=email, password=generate_hash(password))

            try:
                session.add(new_user)
                session.commit()
            except IntegrityError:
                flash('User already exists!')
                return render_template('auth/signup.html', form=form)

            response = make_response(redirect(url_for('general.index')))
            access_token = create_token(identity)
            response.set_cookie('access_token', access_token, path='/')
            if not send_message(email, identity):
                return 'Something wrong! Try again later!'
            flash('Your account confirmation email has been sent to your email!')
            return response
    return render_template('auth/signup.html', title='Signup', form=form)


def login():
    if g.user:
        return redirect('/')

    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():

            username = request.form.get('username', None)
            password = request.form.get('password', None)

            user = session.query(User).filter_by(username=username).first()

            if not user:
                flash('No user found with this username')
                return
            elif not check_hash(password, user.password):
                flash('Wrong password!')
                return render_template('auth/login.html', form=form)

            url = request.args.get('after', None)
            if url:
                response = make_response(redirect(url))
            else:
                response = make_response(redirect(url_for('general.index')))

            access_token = create_token(user.uuid)
            response.set_cookie('access_token', access_token, path='/')

            return response
    return render_template('auth/login.html', title='Login', form=form)


def verification(token):
    if verify(token):
        flash('Your email address has been successfully verified! Now you have all the features of our site, enjoy!')
        return redirect(url_for('general.index'))
    else:
        'Verification token expired! Signup again!'
        #  In the future, I will add support for deleting unverified accounts through redis


def logout():
    response = make_response(redirect(url_for('general.index')))
    response.set_cookie('access_token', '', expires=0)
    return response
