from wtforms import StringField, PasswordField, EmailField, ValidationError
from .validators import validate_username, validate_password, validate_email
from flask_wtf import FlaskForm


class AuthForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    email = EmailField('Email')

    def validate_username(self, field):
        if not validate_username(field.data):
            raise ValidationError('Username should be between 5 and 30 and contain only Latin letters,'
                                  ' numbers and underscores')

    def validate_password(self, field):
        if not validate_password(field.data):
            raise ValidationError('Password must contain at least one uppercase and lowercase letter,'
                                  ' numbers and symbols .,_@$!%*?&')

    def validate_email(self, field):
        if not validate_email(field.data):
            raise ValidationError('Please, write your real correct email address')
