import os
import requests

AIRTABLE_BASE_URL = 'https://api.airtable.com/v0/appnfHuWptUFonq1U/Resources'
API_KEY = os.environ.get('AIRTABLE_API_KEY')

def get_all_resources():
    result = {}
    headers = {'Authorization': "Bearer {}".format(API_KEY)}
    response = requests.get(AIRTABLE_BASE_URL, headers=headers)

    json_response = response.json()

    if response.status_code != 200:
        return {'error': json_response['error']['message']}, response.status_code

    parsed_resources = []
    for resource in json_response['records']:
        if 'Author' in resource['fields'] and 'ResourceContents' in resource['fields']:
            parsed_resources.append({'author': resource['fields']['Author'], 'contents': resource['fields']['ResourceContents']})
    
    result['resources'] = parsed_resources
    
    return result, 200

def create_resource(author, resource_contents):
    headers = {'Authorization': "Bearer {}".format(API_KEY),
                'Content-Type': 'application/json'}
    response = requests.post(AIRTABLE_BASE_URL, headers=headers, json={'fields': {'Author': author, 'ResourceContents': resource_contents}})
    json_response = response.json()

    if response.status_code != 200:
        return {'error': json_response['error']['message']}, response.status_code

    return {'author': json_response['fields']['Author'], 'contents': json_response['fields']['ResourceContents']}, 200
