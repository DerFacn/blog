from flask import Blueprint
from .routes import create_post, view_post

bp = Blueprint('posts', __name__, url_prefix='/posts')

bp.add_url_rule('/create', 'create_post', create_post, methods=['GET', 'POST'])
bp.add_url_rule('/view/<int:post_id>', 'view_post', view_post, methods=['GET'])
