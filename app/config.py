from environs import Env
import jwt

env = Env()

env.read_env()

class config:
    SQLALCHEMY_DATABASE_URI = env.str('DATABASE_URL')
    ENV=env.str('ENV')
    DEBUG=env.bool('DEBUG')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class Token:
    def generate_token(self, data):
        return jwt.encode(data, env.str('SECRET_KEY'), algorithm=env.str('ALGORITHM'))

    def decode_token(self, token):
        return jwt.decode(token, env.str('SECRET_KEY'), algorithm=env.str('ALGORITHM'))