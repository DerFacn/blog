from flask import Blueprint
from .routes import create_post, edit_post, view_post, like_post, delete_post

bp = Blueprint('posts', __name__, url_prefix='/posts')

bp.add_url_rule('/create', 'create_post', create_post, methods=['GET', 'POST'])
bp.add_url_rule('/edit/<int:post_id>', 'edit_post', edit_post, methods=['GET', 'POST'])
bp.add_url_rule('/view/<int:post_id>', 'view_post', view_post, methods=['GET'])
bp.add_url_rule('/like', 'like_post', like_post, methods=['POST'])
bp.add_url_rule('/delete/<string:post_id>', 'delete_post', delete_post, methods=['POST'])
