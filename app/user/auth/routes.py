from flask import request, render_template, flash, make_response, redirect, url_for, g
from .utils import generate_hash, check_hash, create_token
from .forms import SignupForm, LoginForm
from app.models import User
from app.db import session
from .verification import send_message, verify
from app.utils import login_required


def signup():
    if g.user:
        return redirect('/')

    form = SignupForm()
    if request.method == 'POST':
        if form.validate_on_submit():

            username = request.form.get('username', None)
            password = request.form.get('password', None)
            email = request.form.get('email')
            error = False

            username_check = session.query(User).filter_by(username=username).first()
            if username_check:
                error = True
                flash('User with this username already exists!')

            email_check = session.query(User).filter_by(email=email).first()
            if email_check:
                error = True
                flash('User with this email already exists!')

            if error:
                return render_template('auth/signup.html', form=form)

            new_user = User(username=username, email=email, password=generate_hash(password))

            session.add(new_user)
            session.commit()

            response = make_response(redirect(url_for('main.index')))
            access_token = create_token(new_user.uuid)
            response.set_cookie('access_token', access_token, path='/')

            if not send_message(email, new_user.uuid):
                return '<h1">Something wrong! Please, write about this problem to admin!</h1>'
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
                return render_template('auth/login.html', form=form)
            elif not check_hash(password, user.password):
                flash('Wrong password!')
                return render_template('auth/login.html', form=form)

            url = request.args.get('after', None)
            if url:
                response = make_response(redirect(url))
            else:
                response = make_response(redirect(url_for('main.index')))

            access_token = create_token(user.uuid)
            response.set_cookie('access_token', access_token, path='/')

            return response
    return render_template('auth/login.html', title='Login', form=form)


def verification(token):
    if verify(token):
        flash('Your email address has been successfully verified! Now you have all the features of our site, enjoy!')
        return redirect(url_for('main.index'))
    else:
        flash('Your verification token is expired! Write')
        return redirect(url_for('main.index'))
        #  In the future, I will add support for deleting unverified accounts through redis


@login_required
def resend_email_verification(user):
    email = request.form.get('email')
    user.email = email
    send_message(email, user.uuid)
    flash('Your new email confirmation link has been send to your email!')
    return redirect(url_for('main.index'))


def logout():
    response = make_response(redirect(url_for('main.index')))
    response.set_cookie('access_token', '', expires=0)
    return response
