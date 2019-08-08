from flask_restplus import Resource
from ..resources.resources_service import get_all_resources
from ..resources.resources_dto import ResourcesDto

api = ResourcesDto.api
_resources = ResourcesDto.resources

@api.route('/')
class Resources(Resource):
    #@cors.crossdomain(origin='*', methods={"GET"})
    @api.doc('gets the list of all SSE resources')
    @api.marshal_list_with(_resources, envelope='data')
    def get(self):
        return get_all_resources()