#coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from zxscheduler import snscheduler
from zxauths import authbb
from homepage import homepage
from .init import db, lm

lm.session_protection = 'strong'
lm.login_view = 'authbb.login'

DEFAULT_MODULES = (
    (homepage,''),
    (snscheduler, '/snsche'),
    (authbb, '/auth'),


)

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    setting_modules(app, DEFAULT_MODULES)
    db.init_app(app)
    lm.init_app(app)
    return app

def setting_modules(app, modules):
    for module, url_prefix in modules:
        app.register_blueprint(module, url_prefix=url_prefix)


