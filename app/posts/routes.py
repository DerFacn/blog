from flask import request, render_template, redirect, url_for
from .forms import PostForm
from app.models import Post
from app.db import session
from app.utils import login_required


@login_required
def create_post(user):
    form = PostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = request.form.get('title')
            body = request.form.get('body')
            new_post = Post(title=title, body=body, user_uuid=user.uuid)
            session.add(new_post)
            session.commit()
            return f'<h1>{title}</h1><p>{body}</p>'
    return render_template('posts/create.html', form=form)


def view_post(post_id):
    post = session.query(Post).filter_by(id=post_id).first()
    if not post:
        return '<h1 style="text-align: center">404 NOT FOUND</h1>'
    return render_template('posts/post.html', post=post)
