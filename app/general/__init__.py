from flask import Blueprint
from .routes import index

general = Blueprint('general', __name__)

general.add_url_rule('/', 'index', index, methods=['GET'])
