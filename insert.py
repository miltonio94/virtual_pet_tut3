# from pymongo import MongoClient
# # from credentials import database as db
# from datetime import datetime
# import config
#
# uri = "mongodb://test:test@localhost/mytable"
#
# client = MongoClient(uri)
# db = client['mytable']
#
# post = {
#     "author" : "Me",
#     "text" : "Hello Mongo World",
#     "tags" : ["We're", " half ", "way", " there"],
#     "timestamp" : datetime.utcnow()
# }
#
# collection = db.my_post
# collection.insert_one(post)

from pymongo import MongoClient
import datetime

from credentials import db_access

host='ds033390.mlab.com:33390'
db_name = 'tut2'
uri = "mongodb://%s:%s@%s/%s" % (db_access.user, db_access.password, host, db_name)

client = MongoClient(uri)
db = client[db_name]

post = {"name": "Flippy",
        "played": 100,
        "fullness": 100,
        "cuddled": 100,
        "date": datetime.datetime.utcnow()}

collection = db.petStat
collection.insert_one(post)

for x in db.my_posts.find():
    print(x)
