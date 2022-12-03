from flask import Blueprint, redirect, render_template, request, send_from_directory
from flask_login import login_required

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/index', methods=['GET'])
@login_required
def index_page():
    return render_template('index.html')