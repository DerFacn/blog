from flask import Flask
from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return 'Hello, World'


from app.db import session


@app.teardown_appcontext
def shutdown_session(e=None):
    session.remove()


from app.user import user
app.register_blueprint(user)
