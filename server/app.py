#!/usr/bin/env python3

from flask import Flask, jsonify, request, session, make_response
from flask_migrate import Migrate
# from flask_bcrypt import Bcrypt
# from flask_cors import CORS

from models import db

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

# bcrypt = Bcrypt(app)


## ----- HOME PAGE ----- ##

@app.route("/")
def index():
    return "<h1>HOME PAGE</h1>"


## ----- RUN MAIN ----- ##

if __name__ == "__main__":
    app.run(port=5555, debug=True)