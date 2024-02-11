from flask import Blueprint
from .auth import auth
from .routes import me, user_profile

bp = Blueprint('user', __name__, url_prefix='/user')

bp.add_url_rule('/me', 'me', me, methods=['GET', 'POST'])
bp.add_url_rule('/<string:username>', 'user_profile', user_profile, methods=['GET'])

bp.register_blueprint(auth)
