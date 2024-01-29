from flask_mail import Message
from app import mail, app
from app.models import User
from app.db import session
from itsdangerous import URLSafeTimedSerializer
from flask import url_for
from itsdangerous.exc import SignatureExpired


s = URLSafeTimedSerializer(app.config['SERIALIZER_SECRET_KEY'], salt=app.config['SERIALIZER_SECRET_KEY'])


def send_message(email, uuid):
    token = s.dumps(uuid)
    msg = Message(
        'Your verification!',
        recipients=[email]
    )
    url = app.config['DOMAIN'] + url_for('user.auth.verification', token=token)
    msg.html = f'''
    <div style="width: 95%; margin: 0 auto; font-size: 20.4px; text-align: center;">
    <h1>Your email verification link on 🥝Kiwi Blog</h1>

    <a href="{url}" style="cursor: pointer; text-decoration: none; padding: 10px; border: 2px solid #797979; border-radius: 5px;
    display: inline-block; width: 20%; margin: 10px auto 20px auto; color: black">
    <strong>Verify my account!</strong></a><br>

    <strong>If you received this email by mistake
    (You did not register on our site) then simply ignore this email.</strong>
    </div>
    '''
    mail.send(msg)
    return True


def verify(token):
    try:
        uuid = s.loads(token, max_age=7200)
        user = session.query(User).filter_by(uuid=uuid).first()
        user.is_active = True
        session.commit()
        return True
    except SignatureExpired:
        return False
        #  In the future, I will add support for deleting unverified accounts through redis
