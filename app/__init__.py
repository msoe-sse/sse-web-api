from flask import Flask, request
from flask_restful import Resource, Api
from app.GoogleSheetsService import parse_to_json
from app.GoogleDriveService import download_and_parse_to_json
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Points(Resource):
    def get(self):
        type = request.args['type']
        if type == 'sheets':
            return parse_to_json()
        elif type == 'drive':
            return download_and_parse_to_json()

api.add_resource(Points, '/points')
