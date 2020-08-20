import shelve
import os

from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Make an instance of Flask
app = Flask(__name__)

api = Api(app)

# Connects to a database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("people.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

class PeopleList(Resource):
    def get(self): # To show/get data
        shelf = get_db()
        keys = list(shelf.keys())

        people = []

        for key in keys:
            people.append(shelf[key])

        return{'message': "Success", "data": people}, 200

    def post(self): # To add data
        parser = reqparse.RequestParser()

        parser.add_argument('id', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('convo', required=True)

        args = parser.parse_args()

        shelf = get_db()
        shelf[args['id']] = args

        return{'message': "Data registered", 'data': args}, 201


        