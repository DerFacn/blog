from flask import Blueprint
from .auth import auth

bp = Blueprint('user', __name__, url_prefix='/user')

bp.register_blueprint(auth)
