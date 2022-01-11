from flask import Blueprint, render_template, request, redirect, url_for
from extensions import *

friend = Blueprint('friend', __name__, url_prefix="/friends")

# posts = [
#     {'number': 1, 'title': 'Title', 'date': 'today'}
# ]

@friend.route('/')
def friends_index():
    return render_template('/friends/friends_index.html', posts=posts.find())

@friend.route('/new')
def friends_new():
    return render_template('/friends/friends_new.html')

@friend.route('/add_friend', methods=['POST'])
def friends_submit():
    post = {
        'nickname': request.form.get('nickname'),
        'friendcode': request.form.get('friendcode'),
        'title': request.form.get('title'),
        'description': request.form.get('description')
    }
    posts.insert_one(post)
    return redirect(url_for('friend.friends_index'))