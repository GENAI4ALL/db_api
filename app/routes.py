
from flask import Blueprint, request, jsonify
from . import db
from .models import User

main = Blueprint('main', __name__)

@main.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    new_user = User(username=user_data['username'])
    db.session.add(new_user)
    db.session.commit()
    return 'Done', 201

@main.route('/users')
def users():
    user_list = User.query.all()
    users = []
    for user in user_list:
        users.append({'username': user.username})
    return jsonify(users)
