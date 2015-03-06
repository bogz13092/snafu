from flask import Blueprint,abort,make_response

user_bp = Blueprint('user',__name__)

@user_bp.route('/')
def register_user():
	return make_response(open('static/app/index.html').read())