from flask import Blueprint
from app import user, main, posts

router = Blueprint('app', __name__)

router.register_blueprint(user.bp)
router.register_blueprint(main.bp)
router.register_blueprint(posts.bp)
