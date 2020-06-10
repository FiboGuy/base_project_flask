from flask import Blueprint, request, make_response
import json
from .model import db, AuthUser
from src.Utils.AuthDecorators import loginRequired
from app.config import Token
from app.extensions import db

userController = Blueprint('user', __name__, url_prefix='/auth')

# just a simple auth, obviusly is neccesary to validate post values, set cookie expire time, logout, login methods...

@userController.route('/register', methods=['POST'])
def registerUser():
    data = request.get_json()
    try:
        print(data)
        user = AuthUser(username= data['username'], email = data['email'], password = data['password'])
        db.session.add(user)
        db.session.commit()
    except Exception as err:
        print(err)
        return 'bad request'
    return 'ok'

@userController.route('/login', methods=['POST'])
def loginUser():
    data = request.get_json()
    user = AuthUser.query.filter_by(username=data['username']).first()
    if user.checkPassword(data['password']):
        response = make_response('logged succesfully', 200)
        token = Token()
        data = token.generate_token({'user': user.username})
        response.set_cookie('token', data)
    else:
        response = make_response('bad request', 404)
    return response

@userController.route('/rand')
@loginRequired
def rand(user):
    response = make_response({'username': user.username, 'email': user.email}, 200)
    print(request)
    return response

@userController.route('/random')
def rand2():
    print(dir(request))
    print(request.remote_addr)
    return 'ok'