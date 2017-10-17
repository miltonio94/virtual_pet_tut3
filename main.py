from flask import Flask, render_template
from pymongo import MongoClient
from credentials import database as db
import config

LOCAL = False

app = Flask(__name__)

@app.route("/")

def page():
    return "render_template('index.html')"

if LOCAL and __name__ == "__main__":
    app.run(debug=True)
