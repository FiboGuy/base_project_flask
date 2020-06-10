from app.config import Token
from flask import current_app, request, make_response
from src.User.model import AuthUser

token = Token()

def loginRequired(func):
    def wrapper(*args, **kwargs):
        token = request.cookies.get('token')
        response = make_response('Not allowed', 400)
        if token is None:
            return response
        else:
            jwt = Token()
            data = jwt.decode_token(token)
            user = AuthUser.query.filter_by(username=data['user']).first()
            if(user):
                return func(user=user)
        return response
    return wrapper
