from flask import Flask
from src.Utils.BundleCommand import newBundle
from src.User.controller import userController
from .extensions import db
from .config import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    registerControllers(app)
    registerExtensions(app)
    register_commands(app)
    return app

def registerControllers(app):
    app.register_blueprint(userController)

def registerExtensions(app):
    db.init_app(app)

def register_commands(app):
    app.cli.add_command(newBundle)

app = create_app()