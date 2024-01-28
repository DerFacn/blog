from dotenv import load_dotenv
from os import environ

load_dotenv()


class Config:
    SECRET_KEY = environ.get('SECRET_KEY') or 'very_strong_secret_key'
    DATABASE_URI = environ.get('DATABASE_URI') or 'sqlite:///app.db'
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY') or 'very_strong_jwt_secret_key'
