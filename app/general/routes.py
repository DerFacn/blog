from flask import render_template
from app.utils import get_user
from app.db import session
from app.models import Post


@get_user
def index(user):
    all_posts = session.query(Post).all()
    posts = all_posts[::-1]
    return render_template('index.html', user=user, posts=posts)
