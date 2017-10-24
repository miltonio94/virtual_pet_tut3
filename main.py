from flask import Flask, render_template
from pymongo import MongoClient
from credentials import database as db
import config

app = Flask(__name__)

uri = "mongodb://%s:%s@%s/%s" % (db.user, db.password, config.host, config.db_name)

print(uri)

client = MongoClient(uri)
db = client[config.db_name]

for x in db.my_posts.find():
    print x

@app.route("/")

def page():
    return render_template('index.html')

if (not config.ON_HEROKU) and __name__ == "__main__":
    app.run(debug=True)
