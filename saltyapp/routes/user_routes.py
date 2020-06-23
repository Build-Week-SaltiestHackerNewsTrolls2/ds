# saltyapp/routes

from flask import Blueprint, jsonify
import pandas as pd
from saltyapp.model import db, salty_user, salty_comment, parse_records

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

    #result = my_df.loc[username]
    print(result)

    result = salty_user.query.filter_by(Username=username)
    print(type(result.to_json()))

    return result.to_json()


@user_routes.route('/topfive')
def top_five():
    #topfive = my_df.sort_values(by=['saltyscore'])
    topfive = salty_user.query.limit(5).all()
    #data = topfive[:5].to_json()
    data = jsonify(topfive)
    return data


@user_routes.route('/users')
def username_list():
    # print(my_df.to_json(orient='index'))
    # json_df = my_df.to_json(orient='index')
    records = salty_user.query(User_ID, Username).all()
    print('@@@ records', records)
    json_list = parse_records(records)

    return json_list


@user_routes.route('/comment/<username>')
def comment_list(username):
    records = salty_comment.query.filter_by(Username=username)
    comments = parse_records(records)
    json_comments = jsonify(comments)
    return comments
