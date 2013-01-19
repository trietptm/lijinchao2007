#coding:gbk
import pymongo
import datetime
conn = pymongo.Connection(host = "127.0.0.1", port=27017)
db = conn.test_database

collection = db.test_collection

post = {"author": "Mike", "text": "My first blog post!",
          "tags": ["mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}

posts = db.posts

#posts.insert(post)
#collection.insert(post)
print  db.collection_names()
print posts.find_one()

for post in posts.find():
    print post
    
print posts.find_one({"author": "Mike"})