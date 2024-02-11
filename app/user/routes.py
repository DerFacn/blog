from flask import render_template, abort, request, url_for, redirect, flash
from app.utils import login_required
from app.db import session
from app.models import Post, User
from app import app
import os


@login_required
def me(user):
    if request.method == 'POST':
        avatar = request.files.get('avatar', None)
        if len(avatar.read()) > 1_048_576:
            flash('Pick 128x128 image with size less then 100Kb')
            return redirect(url_for('user.me'))
        avatar.seek(0)
        filename = f'{user.uuid}.png'
        avatar.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        user.avatar = filename
        session.commit()
        return redirect(url_for('user.me'))
    my_posts = session.query(Post).filter_by(user_uuid=user.uuid).all()
    posts = my_posts[::-1]
    return render_template('me.html', title='Me', user=user, posts=posts)


def user_profile(username):
    user = session.query(User).filter_by(username=username).first()
    if not user:
        abort(404)
    return render_template('profile.html', title=user.username, user=user)
