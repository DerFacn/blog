import re
from markupsafe import Markup


def order(text: str) -> str:
    cleaned = str(Markup.escape(text))
    formatted_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', cleaned)
    formatted_text = re.sub(r'__(.*?)__', r'<em>\1</em>', formatted_text)
    return formatted_text


def disorder(text: str) -> str:
    _text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text)
    _text = re.sub(r'<em>(.*?)</em>', r'__\1__', _text)
    return _text
