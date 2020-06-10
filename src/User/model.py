from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class AuthUser(db.Model):
    __tablename__ = 'auth_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    __password = db.Column('password', db.String(100), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.setPassword(password)
    
    def __str__(self):
        return 'User {}'.format(self.username)

    def setPassword(self, password):
        self.__password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(pwhash=self.__password, password=password)



