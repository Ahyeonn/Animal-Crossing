from pymongo import MongoClient

client = MongoClient()
db = client.Animal_Crossing

posts = db.posts
comments = db.comments