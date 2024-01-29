from dotenv import load_dotenv
from os import environ

load_dotenv()


class Config:
    DOMAIN = environ.get('DOMAIN') or 'http://127.0.0.1:5000'
    SECRET_KEY = environ.get('SECRET_KEY') or 'very_strong_secret_key'
    DATABASE_URI = environ.get('DATABASE_URI') or 'sqlite:///app.db'
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY') or 'very_strong_jwt_secret_key'
    SERIALIZER_SECRET_KEY = environ.get('SERIALIZER_SECRET_KEY') or 'secret_key_for_verification_function'
    # Mail
    MAIL_SERVER = environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = environ.get('MAIL_PORT') or '465'
    MAIL_USE_SSL = True
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = environ.get('MAIL_DEFAULT_SENDER') or "🥝Kiwi"
