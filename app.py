from flask import Flask

from blueprints.main import main
from blueprints.friend import friend
from blueprints.comment import comment

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(friend)
app.register_blueprint(comment)

if __name__ == '__main__':
    app.run(debug=True)