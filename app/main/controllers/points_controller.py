from flask_restplus import Resource
from ..points.google_sheets_points_service import get_point_data
from ..points.points_dto import PointsDto

api = PointsDto.api
_points = PointsDto.points

@api.route('/points')
class Points(Resource):
    #@cors.crossdomain(origin='*', methods={"GET"})
    @api.doc('gets the list of point data for a quarter')
    @api.marshal_list_with(_points, envelope='data')
    def get(self):
        return get_point_data()