from flask import Flask, request
from flask_restful import Resource, Api
from app.GoogleSheetsService import GoogleSheetsService
from app.GoogleDriveService import download_and_parse_to_json
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)
google_sheets_service = GoogleSheetsService()

class Points(Resource):
    def get(self):
        type = request.args['type']
        if type == 'sheets':
            return google_sheets_service.parse_to_json()
        elif type == 'drive':
            return download_and_parse_to_json()

api.add_resource(Points, '/points')
