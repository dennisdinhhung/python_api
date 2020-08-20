from flask import Flask 
from flask_restful import Api, Resource, reqparse # remember to use pip install flask-restful 
import random

app = Flask(__name__)
api = Api(app)

# Since this is a training script, we will import data straight in. Though, database can be used
ai_quotes = [
    {
        "id": 0,
        "name": "Dennis Dinh",
        "convo": "I hate my self."
    },
    {
        "id": 1,
        "name": "Ziu",
        "convo": "I hate yout guts."
    },
    {
        "id": 2,
        "name": "JSchlatt",
        "convo": "I'm gay."
    },
    {
        "id": 3,
        "name": "Mark Fishbach",
        "convo": "Del Monte... sponsor us."
    }
]

# To check HTMl request, use Postman
class Convo(Resource):
    def get(self, id=0):
        if id==0:
            return random.choice(ai_quotes), 200 #Returns a random convo
            # This returns a "200 OK" status

        for convo in ai_quotes:
            if(convo["id"] == id):
                return convo, 200
            return "No convo found", 404
                # This returns a "404 Not Found" status