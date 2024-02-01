from flask import render_template, request
from app.db import session
from app.models import Post, User


def index():
    all_posts = session.query(Post).order_by(Post.id.desc()).limit(20)
    posts = all_posts[::-1]
    return render_template('index.html', posts=posts)


def search():
    q = request.args.get('q')
    filters = request.args.get('filters', None)

    if filters == 'user':
        records = session.query(User).filter(User.username.ilike(f"%{q}%"))
    else:
        records = session.query(Post).filter(Post.title.ilike(f"%{q}%"))

    return render_template('results.html', title='Results', results=records)
