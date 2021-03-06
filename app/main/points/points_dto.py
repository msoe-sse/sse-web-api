from flask_restplus import Namespace, fields


class PointsDto:
    api = Namespace('points', description='SSE Points related operations')
    students = api.model('students', {
        'name': fields.String(required=True, description='The full name for a student'),
        'pointBreakdown': fields.List(fields.Integer, 
                                       required=True, 
                                       description='An array of ints representings points rewarded for every meeting in a quarter'),
        'pointTotal': fields.Integer(required=True, description='The total number of SSE points a student has earned for a quarter')
    })
    points = api.model('points', {
        'meetings': fields.List(fields.String, required=True, description='The list of meetings for a quarter'),
        'students': fields.List(fields.Nested(students), 
                                required=True, 
                                description='The list of students that have points for a quarter')
    })

