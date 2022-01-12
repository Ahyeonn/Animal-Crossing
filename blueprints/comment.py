from flask import Blueprint, redirect, url_for, request
from bson.objectid import ObjectId
from extensions import *

comment = Blueprint('comment', __name__, url_prefix='/friends')

@comment.route('/comments', methods=['POST'])
def comment_new(): #This post_id is to store post_id from the hidden value
    comment = {
        'post_id': ObjectId(request.form.get('post_id')),
        'comment': request.form.get('comment')
    }
    comments.insert_one(comment)
    return redirect(url_for('friend.friend_show', post_id=request.form.get('post_id'))) 
    #This used for redirect to show page where we passed in post_id as a parameter and got it from the hidden value as well

@comment.route('/comments/<comment_id>', methods=['POST'])
def comments_delete(comment_id):
    comments.delete_one({'_id': ObjectId(comment_id)})
    return redirect(url_for('friend.friend_show', post_id=request.form.get('post_id')))