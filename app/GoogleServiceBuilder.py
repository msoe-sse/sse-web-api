import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

class GoogleServiceBuilder():
    """
    A class for building a google resource object. A resource object is what gives access
    to one of google's api services. This class can handle any of Google's API services
    because they are dependent on the scopes passed into this builder which is a url
    to a given Google API service
    """
    def build_service(self, scopes, service_name, service_version):
        credentials = self._build_credentials(scopes)
        return build(service_name, service_version, credentials=credentials, developerKey=os.environ.get("API_KEY"))

    def build_credentials(self, scopes):
        credentials_raw = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
        service_account_info = json.loads(credentials_raw)
        return service_account.Credentials.from_service_account_info(service_account_info, scopes=scopes)