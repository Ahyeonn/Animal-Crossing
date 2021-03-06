from flask import Blueprint, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from extensions import *
from datetime import datetime

friend = Blueprint('friend', __name__, url_prefix="/friends")

@friend.route('/')
def friends_index():
    return render_template('/friends/friends_index.html', posts=posts.find())

@friend.route('/new')
def friend_new():
    return render_template('/friends/friend_new.html', post={}, title='Add Friend Post')

@friend.route('/add_friend', methods=['POST'])
def friend_submit():
    post = {
        'nickname': request.form.get('nickname'),
        'friendcode': request.form.get('friendcode'),
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'datetime': datetime.now().strftime("%G-%m-%d")
    }
    posts.insert_one(post)
    return redirect(url_for('friend.friend_show', post_id=post['_id']))

@friend.route('/<post_id>')
def friend_show(post_id):
    post = posts.find_one({'_id': ObjectId(post_id)})
    post_comments = comments.find({'post_id': ObjectId(post_id)})
    return render_template('/friends/friend_show.html', post=post, comments=post_comments)

@friend.route('/<post_id>/edit')
def friend_edit(post_id):
    post = posts.find_one({'_id': ObjectId(post_id)})
    return render_template('friends/friend_edit.html', post=post, title='Edit Friend Post')

@friend.route('/<post_id>', methods=['POST'])
def friend_update(post_id):
    updated_post = {
        'nickname': request.form.get('nickname'),
        'friendcode': request.form.get('friendcode'),
        'title': request.form.get('title'),
        'description': request.form.get('description')
    }
    posts.update_one(
        {'_id': ObjectId(post_id)},
        {'$set': updated_post})
    return redirect(url_for('friend.friend_show', post_id=post_id))

@friend.route('/<post_id>/delete', methods=['POST'])
def friend_delete(post_id):
    posts.delete_one({'_id': ObjectId(post_id)})
    return redirect(url_for('friend.friends_index'))

