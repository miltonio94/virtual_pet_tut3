# from flask import Flask, render_template, send_from_directory
# from pymongo import MongoClient
# from credentials import database as db
# import config
#
# app = Flask(__name__)
#
# uri = "mongodb://%s:%s@%s/%s" % (db.user, db.password, config.host, config.db_name)
#
#
# client = MongoClient(uri)
# db = client[config.db_name]
#
#
# @app.route("/js/<path:path>")
# def send_js(path):
#     return send_from_directory('js', path)
#
# @app.route("/")
# def page():
#     return render_template('index.html', data=db.my_post.find())
#
#
# if (not config.ON_HEROKU) and __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, request, render_template, jsonify, send_from_directory
from pymongo import MongoClient, ASCENDING
import datetime
import os

from credentials import db_access

host = "ds113935.mlab.com:13935"
db_name = 'tut2'

uri = "mongodb://%s:%s@%s/%s" % (db_access.user, db_access.password, host, db_name)

print(uri)

client = MongoClient(uri)
db = client[db_name]

ON_HEROKU = "ON_HEROKU" in os.environ

app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/played', methods=['POST'])
def played():
    latest = db.petStat.find().sort({"date": ASCENDING})
    latest = latest[0]
    if(latest.played < 100):
        latest.played = latest.played + 10
    if(latest.played > 100):
        latest.played = 100

    latest.date = datetime.datetime.utcnow()
    collection = db.petStat
    collection.insert_one(latest)


@app.route('/pated', methods=['POST'])
def pated():
    pass


@app.route('/fed', methods=['POST'])
def fed():
    pass

    # if json['data'] == 37:
    #     return jsonify({ 'x' : 56, 'y' : [-200, 55], 'thirty_seven': 'YES'  })
    # else:
    #     return jsonify({ 'x' : 56, 'y' : [-200, 55], 'z' : json['data']  })

@app.route("/")
def page():
    return render_template('index.html', data=db.my_posts.find())

@app.route("/play")
def play():
    return render_template('play.html', data=db.my_posts.find())



    collection = db.petStat
    collection.insert_one(post)

if (not ON_HEROKU) and __name__ == "__main__":
    app.run(debug=True)
