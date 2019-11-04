import os
from airtable import Airtable

airtable = Airtable('appnfHuWptUFonq1U', os.environ.get('RESOURCE_TABLE'))

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

def create_resource(author, resource_contents, message_id):
    """
    Creates a new SSE resource and inserts it into the Airtable database given an author, 
    the contents of the resource, and the message slack id we're saving as a resource
    """
    match = airtable.match('SlackMessageId', message_id)

    if not match:    
        result = airtable.insert({'Author': author, 'ResourceContents': resource_contents, 'SlackMessageId': message_id})

        return {'author': result['fields']['Author'], 'contents': result['fields']['ResourceContents']}, 200
    
    return {'error': 'Message has already been saved as a resource.'}, 400

