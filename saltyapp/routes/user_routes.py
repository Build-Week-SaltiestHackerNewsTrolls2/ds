# saltyapp/routes

from flask import Blueprint, jsonify
import pandas as pd
from saltyapp.model import db, Salty_user, Salty_comment, parse_records, parse_json

user_routes = Blueprint("user_routes", __name__)


@user_routes.route('/')
def user():
    return "hello world"


@user_routes.route('/saltyscore/<username>')
def salty_score(username):
    result = db.session.query(Salty_user.Username, Salty_user.Saltiness).filter(
        Salty_user.Username == username)

    return parse_json(result)  # cannot take out the first index..


@user_routes.route('/topfive')
def top_five():
    topfive = db.session.query(Salty_user.Username, Salty_user.Saltiness).filter(
        Salty_user.Saltiness == '-48%')

    return parse_json(topfive)


@user_routes.route('/users')
def username_list():
    users = db.session.query(Salty_user.User_ID, Salty_user.Username)

    return parse_json(users)


@user_routes.route('/comment/<username>')
def comment_list(username):
    comments = db.session.query(Salty_comment.Username, Salty_comment.Comment,
                                Salty_comment.Saltiness).filter(Salty_comment.Username == username)

    return parse_json(comments)
