from flask import Flask
from flask_restful import Resource, Api
from app.GoogleSheetsService import parse_to_json
from app.GoogleDriveService import download_and_parse_to_json
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Points(Resource):
    def get(self):
        return parse_to_json()

class PointDrive(Resource):
    def get(self):
        return download_and_parse_to_json()

api.add_resource(Points, '/points')
api.add_resource(PointDrive, '/pointsdrive')