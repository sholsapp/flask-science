import logging

from flask import Flask, render_template, jsonify
from flask.ext.restless import APIManager


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


app = Flask(__name__)


# NOTE: The database is just a dictionary in memory. If you want a more
# sophisticated store, think about using SQLite with SQLAlchemy.
database = {}


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/data')
def data():
  return jsonify(database)
