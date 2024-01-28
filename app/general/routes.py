from flask import render_template
from app.utils import get_user, login_required
from app.db import session
from app.models import Post


def index():
    all_posts = session.query(Post).all()
    posts = all_posts[::-1]
    return render_template('index.html', posts=posts)


@login_required
def me(user):
    my_posts = session.query(Post).filter_by(user_uuid=user.uuid).all()
    return render_template('me.html', title='Me', user=user, posts=my_posts)
