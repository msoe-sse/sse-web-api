import os
from airtable import Airtable
import requests

airtable = Airtable('appnfHuWptUFonq1U', 'Resources')

def get_all_resources():
    """
    Returns a dictionary with a list of all SSE resources from the Airtable database
    """
    result = {}
    records = airtable.get_all()

    parsed_resources = []
    for resource in records:
        if 'Author' in resource['fields'] and 'ResourceContents' in resource['fields']:
            parsed_resources.append({'author': resource['fields']['Author'], 'contents': resource['fields']['ResourceContents']})
    
    result['resources'] = parsed_resources
    
    return result, 200

def create_resource(author, resource_contents):
    """
    Creates a new SSE resource and inserts it into the Airtable database given an anthor and 
    the contents of the resource
    """
    result = airtable.insert({'Author': author, 'ResourceContents': resource_contents})

    return {'author': result['fields']['Author'], 'contents': result['fields']['ResourceContents']}, 200

