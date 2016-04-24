#coding:utf-8
from flask import  render_template, request, redirect, url_for, g, flash
from flask_login import login_user, logout_user, current_user

from . import authbb
from .models import User
from ..init import db


@authbb.route('/login', methods=['GET', 'POST'])
def login():
    args = request.args if request.method == 'GET' else request.form
    user = args.get('username')
    if user:
        print current_user
        isuser = User.query.filter_by(name=user, password=args.get('password')).first()
        if  isuser:
            login_user(isuser)
            flash('Logged in successfully.')
            return redirect(url_for('homepage.index'))
    return  render_template('auth/login.html')


@authbb.route('/logout')
def logout():
    logout_user()
    return  redirect(url_for('authbb.login'))


@authbb.route('/register', methods=['GET', 'POST'])
def register():
    args = request.args if request.method == 'GET' else request.form
    name = args.get('username')
    password = args.get('password')
    repassword = args.get('repassword')
    email = args.get('email')
    print name, password, repassword, email, request.method
    if password is not None and password == repassword:
        user = User(name=name,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(request.args.get('next') or url_for('authbb.login'))
    return  render_template('auth/register.html')


