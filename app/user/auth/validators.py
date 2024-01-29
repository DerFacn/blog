import re

patterns = {'username': r'^[0-9a-zA-Z_]{5,30}$',
            'password': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d.,_@$!%*?&]{8,}$',
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'}


def validate_username(value: str) -> bool:
    result = re.match(patterns['username'], value)
    return True if result else False


def validate_password(value: str) -> bool:
    result = re.match(patterns['password'], value)
    return True if result else False


def validate_email(value: str) -> bool:
    result = re.match(patterns['email'], value)
    return True if result else False
