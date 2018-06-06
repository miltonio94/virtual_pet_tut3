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

def getLatest():
    latest = db.petStat.find().sort("date", ASCENDING)
    latest = latest[0]
    return latest

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/played', methods=['POST'])
def played():
    latest = db.petStat.find().sort("date", ASCENDING)
    latest = latest[0]
    newEntry = {
        "name" : latest["name"],
        "played": latest["played"] + 10,
        "fullness": latest["fullness"],
        "cuddled": latest["cuddled"],
        "date" : datetime.datetime.utcnow()
    }
    if(newEntry["played"] > 100):
        newEntry["played"] = 100

    collection = db.petStat
    collection.insert_one(newEntry)

    return jsonify({"ok": 1})


@app.route('/pated', methods=['POST'])
def pated():
    latest = db.petStat.find().sort("date", ASCENDING)
    latest = latest[0]
    newEntry = {
        "name" : latest["name"],
        "played": latest["played"],
        "fullness": latest["fullness"],
        "cuddled": latest["cuddled"] + 5,
        "date" : datetime.datetime.utcnow()
    }
    if(newEntry["cuddled"] > 100):
        newEntry["cuddled"] = 100

    collection = db.petStat
    collection.insert_one(newEntry)

    return jsonify({"ok": 1})


@app.route('/fed', methods=['POST'])
def fed():
    latest = db.petStat.find().sort("date", ASCENDING)
    latest = latest[0]
    newEntry = {
        "name" : latest["name"],
        "played": latest["played"],
        "fullness": latest["fullness"] + 5,
        "cuddled": latest["cuddled"],
        "date" : datetime.datetime.utcnow()
    }
    if(newEntry["fullness"] > 100):
        newEntry["fullness"] = 100

    collection = db.petStat
    collection.insert_one(newEntry)

    return jsonify({"ok": 1})

@app.route('/remove', methods=['POST'])
def remove():
    latest = getLatest()
    newEntry = {
        "name" : latest["name"],
        "played": latest["played"] - 15,
        "fullness": latest["fullness"] - 10,
        "cuddled": latest["cuddled"] - 5,
        "date" : datetime.datetime.utcnow()
    }

    collection = db.petStat
    collection.insert_one(newEntry)

    return jsonify({"ok": 1})

@app.route('/latest', methods=['POST'])
def latest():
    lat = getLatest()
    retVal = {
        "name" : lat["name"],
        "played": lat["played"],
        "fullness": lat["fullness"],
        "cuddled": lat["cuddled"],
        "date" : lat['date']
    }
    return jsonify(retVal)

@app.route("/")
def page():
    return render_template('index.html', data=db.my_posts.find())

@app.route("/play")
def play():
    return render_template('play.html', data=db.my_posts.find())

@app.route("/feed")
def feed():
    return render_template('feed.html', data=db.my_posts.find())

@app.route("/pat")
def pat():
    return render_template('pat.html', data=db.my_posts.find())

@app.route("/stats")
def stats():
    return render_template('stats.html', data=getLatest())



    collection = db.petStat
    collection.insert_one(post)

if (not ON_HEROKU) and __name__ == "__main__":
    app.run(debug=True)
