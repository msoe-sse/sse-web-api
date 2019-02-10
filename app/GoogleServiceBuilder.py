import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

class GoogleServiceBuilder():
    def build_credentials(self, scopes):
        credentials_raw = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
        service_account_info = json.loads(credentials_raw)
        return service_account.Credentials.from_service_account_info(service_account_info, scopes=scopes)

    def build_service(self, scopes, service_name, service_version):
        credentials = self.build_credentials(scopes)
        return build(service_name, service_version, credentials=credentials, developerKey=os.environ.get("API_KEY"))