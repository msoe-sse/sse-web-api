from flask import Flask
from flask_restful import Resource, Api
from GoogleDriveService import parse_to_json
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Points(Resource):
    def get(self):
        return parse_to_json()

api.add_resource(Points, '/points')

if __name__ == '__main__':
     app.run(debug=True)