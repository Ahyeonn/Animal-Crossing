from flask import Flask

from blueprints.main import main
from blueprints.friend import friend
from blueprints.comment import comment
from blueprints.login import user_login

app = Flask(__name__)
app.secret_key = 'mysecretkey'


app.register_blueprint(main)
app.register_blueprint(friend)
app.register_blueprint(comment)
app.register_blueprint(user_login)

if __name__ == '__main__':
    app.run(debug=True)