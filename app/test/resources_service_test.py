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
            'fields': {'Author': 'andy', 'ResourceContents': 'contents'}
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
    def test_create_resource(self, airtable_mock):
        """
        Basic test case for the get_all_resources method in the resource_service
        """
        # Arrange
        airtable_mock.insert.return_value = {
            'fields': {'Author': 'andy', 'ResourceContents': 'contents'}
        }

        # Act
        result = create_resource('andy', 'contents')[0]

        # Assert
        airtable_mock.insert.assert_called_once_with({'Author': 'andy', 'ResourceContents': 'contents'})

        self.assertEqual('andy', result['author'])
        self.assertEqual('contents', result['contents'])

if __name__ == '__main__':
    unittest.main()
