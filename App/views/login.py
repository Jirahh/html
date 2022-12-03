from flask import Blueprint, redirect, render_template, request, send_from_directory
from flask_jwt import jwt_required
from App.models import User
from flask_login import LoginManager
from flask import Flask, flash

from App.controllers import (
    authenticate,
    identity,
    login_user,
    logout_user,
    setup_jwt
)

login_views = Blueprint('login_views', __name__, template_folder='../templates')

@login_views.route('/', methods=['GET'])
def login_page():
    return render_template('login.html')

@login_views.route('/login', methods=['POST'])
def loginAction():
    username=request.form.get('username')
    password=request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        return render_template('index.html')
    else:
        flash('Invalid username or password.')
    return render_template('login.html')