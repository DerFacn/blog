from flask import Blueprint
from app import user, general, posts

router = Blueprint('app', __name__)

router.register_blueprint(user.bp)
router.register_blueprint(general.bp)
router.register_blueprint(posts.bp)
