from flask import Flask, Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from routes import *
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'db.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma =  Marshmallow(app)

app.register_blueprint(routes)

@app.route("/", methods=['GET'])
def get():
    return jsonify({'msg': 'hello world!'})

# run server
if __name__ == "__main__":
    app.run(debug=True)
