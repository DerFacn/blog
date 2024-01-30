from wtforms import StringField, PasswordField, EmailField, ValidationError
from .validators import validate_username, validate_password, validate_email
from flask_wtf import FlaskForm


def username_validator(self, field):
    if not validate_username(field.data):
        raise ValidationError('Username should be between 5 and 30 and contain only Latin letters,'
                              ' numbers and underscores')


def password_validator(self, field):
    if not validate_password(field.data):
        raise ValidationError('Password must contain at least one uppercase and lowercase letter,'
                              ' numbers and symbols .,_@$!%*?&')


def email_validator(self, field):
    if not validate_email(field.data):
        raise ValidationError('Please, write your real correct email address')


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[username_validator])
    password = PasswordField('Password', validators=[password_validator])
    email = EmailField('Email', validators=[email_validator])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[username_validator])
    password = PasswordField('Password', validators=[password_validator])
