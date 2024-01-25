from dotenv import load_dotenv
from os import environ

load_dotenv()


class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY') or 'very_strong_secret_key'
    DATABASE_URI = environ.get('DATABASE_URI') or 'sqlite:///app.db'
