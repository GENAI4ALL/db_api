
from flask_restful import Resource, reqparse
from .models import User
from . import db

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help="Username cannot be blank")

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.query.filter_by(id=user_id).first()
            if user:
                return {'id': user.id, 'username': user.username}
            return {'message': 'User not found'}, 404
        users = User.query.all()
        return [{'id': user.id, 'username': user.username} for user in users]

    def post(self):
        args = parser.parse_args()
        new_user = User(username=args['username'])
        db.session.add(new_user)
        db.session.commit()
        return {'id': new_user.id, 'username': new_user.username}, 201
