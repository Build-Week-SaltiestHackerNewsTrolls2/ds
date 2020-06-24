# saltyapp/routes

from flask import Blueprint, jsonify
import pandas as pd
from saltyapp.model import db, Salty_user, Salty_comment, parse_records

user_routes = Blueprint("user_routes", __name__)
my_df = pd.DataFrame([4.5, 5, -5, -50, 45, 56, 99, 100, -1, -76, 83, 55],
                     index=['luis', 'ilmo', 'becca', 'pyrom', 'daniel', 'kara',
                            'adam', 'zack', 'ethan', 'mistery', 'manny', 'rosa'],
                     columns=['saltyscore']
                     )


@user_routes.route('/')
def user():
    return "hello world"


@user_routes.route('/saltyscore/<username>')
def salty_score(username):
    print(username)
    result = db.session.query(Salty_user.Username, Salty_user.Saltiness).filter(Salty_user.Username == username).one()
    print(jsonify(result))

    return jsonify(result)


@user_routes.route('/topfive')
def top_five():
    topfive = db.session.query(Salty_user.Username, Salty_user.Saltiness).filter(Salty_user.Saltiness == '-48%').all()
    print(topfive)
    data = jsonify(topfive)
    print(data)
    return data


@user_routes.route('/users')
def username_list():
    records = db.session.query(Salty_user.User_ID, Salty_user.Username).all()
    print('here', jsonify(records))
    return jsonify(records)


@user_routes.route('/comment/<username>')
def comment_list(username):
    comments = db.session.query(Salty_comment.Username, Salty_comment.Comment, Salty_comment.Saltiness).filter(Salty_comment.Username==username).all()
    print(jsonify(comments))
    return jsonify(comments)
