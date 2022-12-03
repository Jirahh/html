from flask import Blueprint, redirect, render_template, request, send_from_directory
from flask_jwt import jwt_required

signup_views = Blueprint('signup_views', __name__, template_folder='../templates')

@signup_views.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@signup_views.route('/signup', methods=['POST'])
def signupAction():
    data = request.form
    newuser = User(username=data['username'], email=data['email'])
    newuser.set_password(data['password'])
    try:
        db.session.add(newuser)
        db.session.commit()
        login_user(newuser)
        flash('Account Created!')
        return redirect(url_for('get_app'))
    except IntegrityError:
        db.session.rollback()
        flash("Username or Email already exists")
    return redirect(url_for('get_app'))