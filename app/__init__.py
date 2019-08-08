from flask_restplus import Api
from flask import Blueprint

from .main.controllers.points_controller import api as points_ns
from .main.controllers.resources_controller import api as resources_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='SSE Website API',
          version='1.0',
          description='A API used for the MSOE Society of Software Engineers Website')

api.add_namespace(points_ns, path='/points')
api.add_namespace(resources_ns, path='/resources')
