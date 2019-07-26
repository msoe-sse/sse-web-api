from flask_restplus import Api
from flask import Blueprint

from .main.controllers.points_controller import Api as points_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='SSE Website API',
          version='1.0',
          description='A API used for the MSOE Society of Software Engineers Website')

api.add_namespace(points_ns, path='/points')
