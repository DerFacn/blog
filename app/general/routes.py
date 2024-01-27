from flask import render_template
from app.utils import get_user


@get_user
def index(user):
    return render_template('index.html', user=user)
