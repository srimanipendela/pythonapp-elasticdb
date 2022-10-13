from elasticsearch import Elasticsearch
from flask import Flask, jsonify, request
from marshmallow import Schema, fields, ValidationError

import json
import os

app = Flask(__name__)

es = Elasticsearch('http://'+ os.environ['elasticsearchsvc'] + ':'+ os.environ['elasticsearchport'])

index_name = "db"

class BaseSchema(Schema):
    city = fields.String(required=True)

class ExtendedSchema(BaseSchema):
    population = fields.Integer(required=True)

def essearch(city):
    query = {'query': {'match': { 'city':city}}}
    data = es.search(index=index_name,body=query)
    if data['hits']['total']['value'] == 0:
        return "noentry", 0
    else:
        return "entry", data['hits']['hits'][0]['_source']['population']

@app.route('/health')
def health() -> str:
    return "OK", 200

@app.route('/add_data', methods=['POST'])
def add() -> str:
    data = request.get_json()
    schema = ExtendedSchema()

    try:
        schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    if es.ping():
        essearchdata = essearch(data['city'])
        if essearchdata[0] == "noentry":
            es.index(index=index_name,body=data)
            return jsonify("Suceessfully Inserted the give data in DB"), 201
        else:
            return jsonify({"Data Already Exist in DB for the city": data['city']}), 409
    else:
        return jsonify(" Internal Server Error. Prbolem with the DB "), 500

@app.route('/get', methods=['GET'])
def get_population() -> int:
    data = request.get_json()
    schema = BaseSchema() 

    try:
        schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    if es.ping():
        essearchdata = essearch(data['city'])
        if essearchdata[0] == "entry":
            return jsonify({"population of the city" :  essearchdata[1]}), 200
        else:
            return jsonify("Entry not found for the requested city"), 404
    else:
        return jsonify(" Internal Server Error. Prbolem with the DB "), 500

if __name__ == '__main__':
    es.indices.create(index=index_name, ignore=400)
    app.run(host='0.0.0.0')
