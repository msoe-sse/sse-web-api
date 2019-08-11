from flask_restplus import Resource
from ..resources.resources_service import get_all_resources, create_resource
from ..resources.resources_dto import ResourcesDto

api = ResourcesDto.api
_resources = ResourcesDto.resources
_resource = ResourcesDto.resource

@api.route('/')
class Resources(Resource):
    #@cors.crossdomain(origin='*', methods={"GET"})
    @api.doc('gets the list of all SSE resources')
    @api.marshal_list_with(_resources, envelope='data')
    def get(self):
        return get_all_resources()
    
    #@cors.crossdomain(origin='*', methods={"GET"})
    @api.doc('creates a new SSE resource')
    @api.expect(_resource)
    def post(self):
        return create_resource(api.payload['author'], api.payload['contents'])
