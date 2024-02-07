from flask import request, render_template, redirect, url_for, abort, flash
from .forms import PostForm
from app.models import Post
from app.db import session
from app.utils import login_required


@login_required
def create_post(user):
    if not user.is_active:
        flash('Verify your account for writing posts!')
        return redirect(url_for('main.index'))

    form = PostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = request.form.get('title')
            body = request.form.get('body')
            new_post = Post(title=title, body=body, user_uuid=user.uuid)
            session.add(new_post)
            session.commit()
            return redirect(url_for('posts.view_post', post_id=new_post.id))
    return render_template('posts/create.html', title='Creating', form=form)


@login_required
def edit_post(user, post_id):
    post = session.query(Post).filter_by(id=post_id).first()
    if not post:
        abort(404)
    elif post.user_uuid != user.uuid:
        abort(403)
    form = PostForm(title=post.title, body=post.body)
    if request.method == 'POST':
        if form.validate_on_submit():
            title = request.form.get('title')
            body = request.form.get('body')
            post.title = title
            post.body = body
            session.commit()
            return redirect(url_for('posts.view_post', post_id=post.id))
    return render_template('posts/create.html', title='Edit post', form=form)



@login_required
def delete_post(user, post_id):
    post = session.query(Post).filter_by(id=int(post_id)).first()
    session.delete(post)
    session.commit()
    return redirect(url_for('user.me'))


def view_post(post_id):
    post = session.query(Post).filter_by(id=post_id).first()
    if not post:
        abort(404)
    return render_template('posts/post.html', title=f'{post.title}', post=post)
