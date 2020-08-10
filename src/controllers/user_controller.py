from flask import request, jsonify
from app import db

from models.user import User


class UserController():
    
    def index(self):
        users = User.query.all()
        return jsonify([user.serialize() for user in users])

    def store(self):

        user_request = request.json 

        user = User(
            user_request["name"], 
            user_request["email"]
        )

        db.session.add(user)
        db.session.commit()

        return user.serialize()

    def delete(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return user.serialize()