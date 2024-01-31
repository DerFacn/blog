from flask import render_template, abort
from app.utils import login_required
from app.db import session
from app.models import Post, User


@login_required
def me(user):
    my_posts = session.query(Post).filter_by(user_uuid=user.uuid).all()
    posts = my_posts[::-1]
    return render_template('me.html', title='Me', user=user, posts=posts)


def user_profile(username):
    user = session.query(User).filter_by(username=username).first()
    if not user:
        abort(404)
    return render_template('profile.html', title=user.username, user=user)
