from flask_restplus import Namespace, fields

class ResourcesDto:
    api = Namespace('resources', description='SSE Resources related operations')
    resource = api.model('resource', {
        'author': fields.String(required=True, description='The person who orginally shared the resources'),
        'contents': fields.String(required=True, description='The contents of a resource')
    })
    resources = api.model('resources', {
        'resources': fields.List(fields.Nested(resource),
                                 required=True,
                                 description='The total list of SSE Resources')
    })
    