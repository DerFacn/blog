from flask import Flask

app = Flask(__name__)
app.secret_key = 'blog'


@app.route('/')
def index():
    return 'Hello, World'


from app.user import user
app.register_blueprint(user)
