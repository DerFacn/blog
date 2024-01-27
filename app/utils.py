from functools import wraps
from flask import request
import jwt
from jwt.exceptions import ExpiredSignatureError
from app import app
from app.models import User
from app.db import session


def get_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        kwargs['user'] = None
        access_token = request.cookies.get('access_token', None)
        if not access_token:
            return func(*args, **kwargs)
        try:
            payload = jwt.decode(access_token, app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        except ExpiredSignatureError:
            return func(*args, **kwargs)
        user = session.query(User).filter_by(uuid=payload['uuid']).first()
        if not user:
            return func(*args, **kwargs)
        kwargs['user'] = user
        return func(*args, **kwargs)
    return wrapper
