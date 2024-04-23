
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api = Api(app)

    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    from .resources import UserResource
    api.add_resource(UserResource, '/users', '/users/<int:user_id>')

    return app
