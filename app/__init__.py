from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_restful.utils import cors
from app.GoogleSheetsService import GoogleSheetsService
from app.GoogleDriveService import GoogleDriveService
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Points(Resource):
    @cors.crossdomain(origin='*', methods={"GET"})
    def get(self):
        type = request.args['source']
        if type == 'sheets':
            google_sheets_service = GoogleSheetsService()
            return jsonify(google_sheets_service.get_point_data())
        elif type == 'drive':
            google_drive_service = GoogleDriveService()
            return jsonify(google_drive_service.get_point_data())

api.add_resource(Points, '/points')
