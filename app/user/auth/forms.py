from wtforms import StringField, PasswordField, ValidationError
from .validators import validate_username, validate_password
from flask_wtf import FlaskForm


class AuthForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')

    def validate_username(self, field):
        if not validate_username(field.data):
            raise ValidationError('Username should be between 5 and 30 and contain only Latin letters,'
                                  ' numbers and underscores')

    def validate_password(self, field):
        if not validate_password(field.data):
            raise ValidationError('Password must contain at least one uppercase and lowercase letter,'
                                  ' numbers and symbols .,_@$!%*?&')
