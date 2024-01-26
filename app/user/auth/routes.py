from flask import request, render_template, flash, make_response, redirect, url_for
from .utils import generate_hash, check_hash, create_token
from .forms import AuthForm
from app.models import User
from app.db import session
from sqlalchemy.exc import IntegrityError
from uuid import uuid4


def signup():
    form = AuthForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form.get('username', None)
            password = request.form.get('password', None)
            identity = str(uuid4())
            new_user = User(uuid=identity, username=username, password=generate_hash(password))
            try:
                session.add(new_user)
                session.commit()
            except IntegrityError:
                flash('User already exists!')
                return render_template('auth/signup.html', form=form)
            response = make_response(redirect(url_for('index')))
            access_token = create_token(identity)
            response.set_cookie('access_token', access_token, path='/')
            return response
    return render_template('auth/signup.html', form=form)


def login():
    form = AuthForm()
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
            access_token = create_token(user.uuid)
            response = make_response(redirect(url_for('index')))
            response.set_cookie('access_token', access_token, path='/')
    return render_template('auth/login.html', form=form)


def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('access_token', '', expires=0)
    return response
