from flask import Blueprint, render_template
from extensions import *

friend = Blueprint('friend', __name__, url_prefix="/friends")

# posts = [
#     {'number': 1, 'title': 'Title', 'date': 'today'}
# ]

@friend.route('/')
def friend_index():
    return render_template('/friends/friends_index.html', posts=posts.find())