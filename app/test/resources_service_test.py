import unittest
from unittest.mock import patch
from app.main.resources.resources_service import get_all_resources, create_resource

class ResourcesServiceTest(unittest.TestCase):
    @patch('app.main.resources.resources_service.airtable')
    def test_get_all_resources(self, airtable_mock):
        """
        Basic test case for the get_all_resources method in the resource_service
        """
        # Arrange
        airtable_response = [{
            'fields': {}
        }, {
            'fields': {'Author': 'andy'}
        }, {
            'fields': {'ResourceContents': 'contents'}
        }, {
            'fields': {'Id': 1, 'Author': 'andy', 'ResourceContents': 'contents', 'SlackMessageId': "messageId"}
        }]

        airtable_mock.get_all.return_value = airtable_response

        # Act
        result = get_all_resources()[0]

        # Assert
        airtable_mock.get_all.assert_called_once()

        self.assertTrue('resources' in result)
        self.assertEqual(1, len(result['resources']))
        self.assertEqual('andy', result['resources'][0]['author'])
        self.assertEqual('contents', result['resources'][0]['contents'])
    
    @patch('app.main.resources.resources_service.airtable')
    def test_create_resource_success(self, airtable_mock):
        """
        Basic test case for the create_resource method in the resource_service
        """
        # Arrange
        airtable_mock.match.return_value = {}
        airtable_mock.insert.return_value = {
            'fields': {'Author': 'andy', 'ResourceContents': 'contents', 'SlackMessageId': 'id'}
        }

        # Act
        result = create_resource('andy', 'contents', 'id')

        # Assert
        airtable_mock.insert.assert_called_once_with({'Author': 'andy', 'ResourceContents': 'contents', 'SlackMessageId': 'id'})

        self.assertEqual('andy', result[0]['author'])
        self.assertEqual('contents', result[0]['contents'])
        self.assertEqual(200, result[1])
    
    @patch('app.main.resources.resources_service.airtable')
    def test_create_resource_duplicate_message(self, airtable_mock):
        """
        Test Case for the create_resource where the message being saved already exists in Airtable
        """
        # Arrange
        airtable_mock.match.return_value = {'fields': {'SlackMessageId': 'id'}}
        airtable_mock.insert.return_value = {
            'fields': {'Author': 'andy', 'ResourceContents': 'contents', 'SlackMessageId': 'id'}
        }

        # Act
        result = create_resource('andy', 'contents', 'id')

        # Assert
        self.assertFalse(airtable_mock.insert.called)

        self.assertEqual('Message has already been saved as a resource.', result[0]['error'])
        self.assertEqual(400, result[1])

if __name__ == '__main__':
    unittest.main()
