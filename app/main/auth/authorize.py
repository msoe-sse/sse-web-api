from functools import wraps
from flask import request
import os

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if 'Authorization' not in request.headers:
            return {'error': 'Unauthorized'}, 401
        
        token = str.replace(request.headers['Authorization'], 'Bearer ', '')

        if token != os.getenv('SSE_API_KEY'):
            return {'error': 'Unauthorized'}, 401
        
        return f(*args, **kws)
    decorated_function.__doc__ = f.__doc__
    decorated_function.__name__ = f.__name__
    return decorated_function
        