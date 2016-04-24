#!/usr/bin/env python
#coding:utf-8
from ..init import db, lm
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    users = db.relationship('User', backref='role')

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(50))
    password = db.Column(db.String(20))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # @property
    # def password(self):
    #     raise AttributeError('password is not a readable attribute')
    #
    # @password.setter
    # def password(self, password):
    #     self.password = generate_password_hash(password)

@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




