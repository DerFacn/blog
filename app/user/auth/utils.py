from bcrypt import gensalt, hashpw, checkpw
from datetime import datetime, timedelta
import jwt


# Passwords
def generate_hash(password: str) -> bytes:
    salt = gensalt()
    password_bytes = password.encode('utf-8')
    password_hash = hashpw(password_bytes, salt)
    return password_hash


def check_hash(password: str, password_hash: bytes) -> bool:
    password_bytes = password.encode('utf-8')
    return checkpw(password_bytes, password_hash)


from app import app


# Cookie token
def create_token(identity):
    payload = {
        'uuid': identity,
        'exp': datetime.now() + timedelta(weeks=12)
    }
    return jwt.encode(payload, app.config['JWT_SECRET_KEY'], algorithm='HS256')
