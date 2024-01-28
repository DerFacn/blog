from flask import Blueprint
from .routes import index, me

bp = Blueprint('general', __name__)

bp.add_url_rule('/', 'index', index, methods=['GET'])
bp.add_url_rule('/me', 'me', me, methods=['GET'])
