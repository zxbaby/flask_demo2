from flask import render_template, g
from . import homepage
from flask_login import login_required, current_user

@homepage.route('/')
@login_required
def index():
    user = g.user
    return render_template('homepage/index.html', user=user)