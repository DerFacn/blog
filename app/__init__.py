from flask import Flask, g
from app.config import Config
from flask_mail import Mail
from flask_admin import Admin
from flask_babel import Babel


app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
babel = Babel(app)


from app.db import session
from app.admin_panel import CustomAdminIndexView, user_view, post_view

admin = Admin(app, name='Blog', template_mode='bootstrap3', index_view=CustomAdminIndexView(endpoint='/admin_panel'))
admin.add_view(user_view)
admin.add_view(post_view)


@app.teardown_appcontext
def shutdown_session(e=None):
    session.remove()


from app.utils import get_user  # Imports here are due to circular imports


@app.before_request
@get_user
def before_request(user):
    g.user = user


from app.errors import app


from app import user, general, posts
app.register_blueprint(general.bp)
app.register_blueprint(user.bp)
app.register_blueprint(posts.bp)


from app.commands import create_admin_command
app.cli.add_command(create_admin_command)
