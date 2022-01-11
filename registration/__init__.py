from flask import Flask, Blueprint

from .main import main
from .friend import friend

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main)
    app.register_blueprint(friend)
        
    return app

if __name__ == '__main__':
    app.run(debug=True)