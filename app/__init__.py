from flask import Flask
from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)


from app.db import session


@app.teardown_appcontext
def shutdown_session(e=None):
    session.remove()


from app import user, general
app.register_blueprint(general.general)
app.register_blueprint(user.user)
