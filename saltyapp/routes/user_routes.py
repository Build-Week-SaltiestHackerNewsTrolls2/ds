#saltyapp/routes

from flask import Blueprint, jsonify
import pandas as pd

user_routes = Blueprint("user_routes", __name__)

my_df = pd.DataFrame([4.5, 5, -5, -50, 45, 56, 99, 100, -1, -76, 83, 55],
index=['luis', 'ilmo', 'becca', 'pyrom', 'daniel', 'kara', 'adam', 'zack', 'ethan', 'mistery', 'manny', 'rosa'],
columns=['saltyscore']
)

@user_routes.route('/')
def user():
    return "hello world"

@user_routes.route('/saltyscore/<username>')
def salty_score(username):
    print(username)

    result = my_df.loc[username]
    print(result)
    print(type(result.to_json()))
    return result.to_json()

@user_routes.route('/topfive')
def top_five():
    topfive = my_df.sort_values(by=['saltyscore'])
    data = topfive[:5].to_json()
    return data


def username_list():
    pass
