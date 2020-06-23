#saltyapp/__init__.py

from flask import Flask
from saltyapp.routes.user_routes import user_routes
import os
from dotenv import load_dotenv

# how to hook db into flask reference
# https://vsupalov.com/flask-sqlalchemy-postgres/

load_dotenv()

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

DB_URL = 'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_routes)

    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)

    return app

if __name__ =="__main__":
    myapp = create_app()
    myapp.run(debug=True)
