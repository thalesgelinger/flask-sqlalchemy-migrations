from flask import jsonify
from app import db

import json

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def serialize(self):
        return jsonify({
            "id": self.id,
            "name": self.name,
            "email": self.email
        })