from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_restful.utils import cors
from app.GoogleSheetsPointsService import GoogleSheetsPointsService
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Points(Resource):
    def __init__(self):
        self.sheets_service = GoogleSheetsPointsService()

    @cors.crossdomain(origin='*', methods={"GET"})
    def get(self):
        return jsonify(self.sheets_service.get_point_data())


api.add_resource(Points, '/points')
