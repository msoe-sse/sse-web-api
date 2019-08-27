import os
from airtable import Airtable
import requests

airtable = Airtable('appnfHuWptUFonq1U', 'Resources')
AIRTABLE_BASE_URL = 'https://api.airtable.com/v0/appnfHuWptUFonq1U/Resources'
API_KEY = os.environ.get('AIRTABLE_API_KEY')

def get_all_resources():
    result = {}
    records = airtable.get_all()

    parsed_resources = []
    for resource in records:
        if 'Author' in resource['fields'] and 'ResourceContents' in resource['fields']:
            parsed_resources.append({'author': resource['fields']['Author'], 'contents': resource['fields']['ResourceContents']})
    
    result['resources'] = parsed_resources
    
    return result, 200

def create_resource(author, resource_contents):
    result = airtable.insert({'Author': author, 'ResourceContents': resource_contents})

    return {'author': result['fields']['Author'], 'contents': result['fields']['ResourceContents']}, 200

