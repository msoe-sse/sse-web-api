from flask_restplus import Namespace, Fields


class PointsDto:
    api = Namespace('points', description='SSE Points related operations')
    student_fields = {
        'name': fields.String(required=True, description='The full name for a student'),
        'pointsBreakdown': fields.List(fields.Int, 
                                       required=True, 
                                       description='An array of ints representings points rewarded for every meeting in a quarter'),
        'pointTotal': fields.Int(required=True, description='The total number of SSE points a student has earned for a quarter')
    }
    points = api.model('points', {
        'meetings': fields.List(fields.String, required=True, description='The list of meetings for a quarter'),
        'students': fields.List(fields.Nested(student_fields), 
                                required=True, 
                                description='The list of students that have points for a quarter')
    })

