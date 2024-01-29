from flask import Blueprint
from .routes import signup, login, logout, verification

auth = Blueprint('auth', __name__, url_prefix='/auth')

auth.add_url_rule('/signup', 'signup', signup, methods=['GET', 'POST'])
auth.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
auth.add_url_rule('/logout', 'logout', logout, methods=['POST'])
auth.add_url_rule('/verif/<string:token>', 'verification', verification, methods=['GET'])
