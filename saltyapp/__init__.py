# saltyapp/__init__.py

from saltyapp.routes import user_routes
from saltyapp.model import db
from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()

# how to hook db into flask reference
# https://vsupalov.com/flask-sqlalchemy-postgres/
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

DB_URL = 'postgres://{user}:{pw}@{host}:5432/{name}'.format(user=DB_USERNAME, pw=DB_PASSWORD, host=DB_HOST, name=DB_NAME)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_routes.user_routes)
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False
    return app


if __name__ == "__main__":
    myapp = create_app()
    myapp.run(debug=True)
