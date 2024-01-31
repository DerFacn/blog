from flask import Blueprint
from .routes import index

bp = Blueprint('general', __name__)

bp.add_url_rule('/', 'index', index, methods=['GET'])
