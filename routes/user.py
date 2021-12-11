from flask import Flask, Blueprint, request, jsonify
from schemes import *
from . import routes

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@routes.route("/user/", methods=['GET'])
def get_users():
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result.data)

@routes.route("/user/", methods=['POST'])
def create_user():
    email = request.json['email']
    username = request.json['username']
    new_user = User(email, username, password)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

@routes.route("/user/<id>", methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

@routes.route("/user/<id>", methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    user.active = True
    db.session.commit()
    return user_schema.jsonify(user)

@routes.route("/user/<id>", methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'msg': 'user deleted'})
