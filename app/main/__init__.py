from flask import Blueprint
from .routes import index, search

bp = Blueprint('main', __name__)

bp.add_url_rule('/', 'index', index, methods=['GET'])
bp.add_url_rule('/search', 'search', search, methods=['GET'])
