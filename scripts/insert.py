# use mytable
# db.createUser({user:"test", pwd:"test", roles:["readWrite"]})

from pymongo import MongoClient
import datetime

uri = "mongodb://test:test@localhost/mytable"

client = MongoClient(uri)
db = client["mytable"]

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

collection = db.my_posts
collection.insert_one(post)

for x in db.my_posts.find():
print(x)
