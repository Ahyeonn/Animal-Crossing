from flask import Flask

from blueprints.main import main
from blueprints.friend import friend

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(friend)

if __name__ == '__main__':
    app.run(debug=True)