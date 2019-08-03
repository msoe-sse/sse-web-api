import os
import requests

AIRTABLE_BASE_URL = 'https://api.airtable.com/v0/appnfHuWptUFonq1U/Resources'
API_KEY = os.environ.get('AIRTABLE_API_KEY')

def get_all_resources():
    result = {}
    headers = {'Authorization': "Bearer {}".format(API_KEY)}
    response = requests.get(AIRTABLE_BASE_URL, headers=headers)
    json_response = response.json()

    parsed_resources = []
    for resource in json_response['records']:
        parsed_resources.append({'author': resource['fields']['Author'], 'contents': resource['fields']['ResourceContents']})
    
    result['resources'] = parsed_resources
    
    return result, 200

def create_resource(author, resource_contents):
    pass
