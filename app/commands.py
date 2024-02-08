import click
from flask.cli import with_appcontext
from sqlalchemy.exc import IntegrityError
from app.user.auth.utils import generate_hash
from app.db import session
from app.models import User
from uuid import uuid4


@click.command('create-admin', help='Create admin user')
@click.argument('username', required=True)
@click.argument('email', required=True)
@click.password_option()
@with_appcontext
def create_admin_command(username, email, password):
    identity = str(uuid4())
    new_user = User(uuid=identity, username=username, password=generate_hash(password), email=email,
                    is_active=1, is_admin=1)
    try:
        session.add(new_user)
        session.commit()
    except IntegrityError:
        print(f'User {username} already exists!')
    print(f'Admin user {username} created!')
