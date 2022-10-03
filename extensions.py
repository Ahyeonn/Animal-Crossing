from pymongo import MongoClient
import os


uri = os.environ.get('MONGODB_URI', 'mongodb://localhost/AC')
client = MongoClient(uri)
db = client.get_default_database()

posts = db.posts
comments = db.comments
users = db.users