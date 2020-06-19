#saltyapp/routes

from flask import Blueprint, jsonify
import pandas as pd

user_routes = Blueprint("user_routes", __name__)

@user_routes.route('/')
def user():
    return "hello world"

@user_routes.route('/saltyscore/<username>')
def salty_score(username):
    print(username)
    my_df = pd.DataFrame([4.5, 5, -5],
    index=['luis', 'ilmo', 'becca'],
    columns=['saltyscore']
    )

    result = my_df.loc[username]
    print(result)
    print(type(result.to_json()))
    return result.to_json()

def username_list():
    pass
