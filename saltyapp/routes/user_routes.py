#saltyapp/routes

from flask import Blueprint, jsonify

user_routes = Blueprint("user_routes", __name__)

@user_routes.route('/')
def user():
    return "hello world"
