from pymongo import MongoClient
from credentials import database as db
from datatime import datetime
import config

uri  = "mongodb://%s:%s@%s/%s" % (db.user, db.password, config.host, config.db_name)

client = MongoClient(uri)
db = client[config.db_name]

post = {
    "author" : "Me",
    "text" : "Hello Mongo World",
    "tags" : ["We're", " half ", "way", " there"],
    "timestamp" : datetime.utcnow()
}

collection = db.my_post
collection.insert_one(post)
