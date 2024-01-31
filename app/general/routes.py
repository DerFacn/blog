from flask import render_template
from app.db import session
from app.models import Post


def index():
    all_posts = session.query(Post).all()
    posts = all_posts[::-1]
    return render_template('index.html', posts=posts)
