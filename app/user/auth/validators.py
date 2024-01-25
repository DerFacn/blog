import re

patterns = {'username': r'^[0-9a-zA-Z_]{5,30}$',
            'password': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d.,_@$!%*?&]{8,}$'}


def validate_username(value: str) -> bool:
    result = re.match(patterns['username'], value)
    return True if result else False


def validate_password(value: str) -> bool:
    result = re.match(patterns['password'], value)
    return True if result else False
