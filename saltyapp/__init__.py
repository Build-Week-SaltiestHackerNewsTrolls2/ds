#saltyapp/__init__.py

from flask import Flask
from saltyapp.routes.user_routes import user_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_routes)
    return app

if __name__ =="__main__":
    myapp = create_app()
    myapp.run(debug=True)
