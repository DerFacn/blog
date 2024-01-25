from flask import Blueprint
from .auth import auth

user = Blueprint('user', __name__, url_prefix='/user')

user.register_blueprint(auth)
