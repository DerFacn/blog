from flask import g
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from app.models import User, Post
from app.db import session


def is_admin():
    return g.user.is_admin


def get_user_uuid():
    return g.user.uuid


class ProtectedModelView(ModelView):
    def is_accessible(self):
        return is_admin()


class PostModelView(ProtectedModelView):
    def on_model_change(self, form, model, is_created):
        if is_created:
            current_user_uuid = get_user_uuid()
            model.user_uuid = current_user_uuid


class CustomAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return is_admin()


user_view = ProtectedModelView(User, session, name='users', endpoint='user_view')
post_view = PostModelView(Post, session, name='posts', endpoint='post_view')
