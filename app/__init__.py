from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_restful.utils import cors
from app.GoogleSheetsPointsService import GoogleSheetsPointsService
from app.GoogleDrivePointsService import GoogleDrivePointsService
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Points(Resource):
    def __init__(self):
        self.sheets_service = GoogleSheetsPointsService()
        self.drive_service = GoogleDrivePointsService()

    @cors.crossdomain(origin='*', methods={"GET"})
    def get(self):
        type = request.args['source']
        if type == 'sheets':
            return jsonify(self.sheets_service.get_point_data())
        elif type == 'drive':
            return jsonify(self.drive_service.get_point_data())

api.add_resource(Points, '/points')
