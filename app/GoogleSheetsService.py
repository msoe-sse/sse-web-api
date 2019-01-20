import os
import json
import google.auth
from googleapiclient.discovery import build
from google.oauth2 import service_account
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client import file, client, tools

SCOPE = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = '1EkZkQogMIfVETUQUzkwoPPfGKF6kjhVhuWsp4EuYDTc'
RANGE_NAME = 'Sheet1!A1:M68'

def parse_to_json():
    parsed_result = {}
    
    credentials_raw = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    service_account_info = json.loads(credentials_raw)
    credentials = service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPE)

    service = build('sheets', 'v4', credentials=credentials, developerKey=os.environ.get("API_KEY"))

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    if values:
        meetings = []
        first_row = values[0]
        for column in first_row:
            if column != "" and column != "TOTALS":
                list.append(meetings, column)
        
        parsed_result["meetings"] = meetings

        students = []
        for i in range(1, len(values)):
            row = values[i]
            current_student = {}
            current_point_breakdown = []
            for j in range(len(row)):
                if j == 0:
                    current_student["name"] = row[j]
                elif j == len(row) - 1:
                    current_student["pointTotal"] = int(row[j])
                else:
                    value_to_append = row[j]
                    if value_to_append == "":
                        value_to_append = 0
                    else:
                        value_to_append = int(value_to_append)
                    list.append(current_point_breakdown, value_to_append)
            current_student["pointBreakdown"] = current_point_breakdown
            list.append(students, current_student)
        
        parsed_result["students"] = sorted(students, key = lambda x: (x['pointTotal'], x['name']), reverse=True)

    return parsed_result