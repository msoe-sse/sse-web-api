from flask_restplus import Api
from flask import Blueprint
from flask_cors import CORS

from .main.controllers.points_controller import api as points_ns
from app.main import create_app

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='SSE Website API',
          version='1.0',
          description='A API used for the MSOE Society of Software Engineers Website')

api.add_namespace(points_ns, path='/points')

app = create_app()
app.register_blueprint(blueprint)

app.app_context().push()

CORS(app, resources={r"/*": {"origins": "*"}})