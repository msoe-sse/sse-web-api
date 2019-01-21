import os
import json
import io
import openpyxl
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload
from app.GoogleServiceBuilder import GoogleServiceBuilder

SCOPES = ['https://www.googleapis.com/auth/drive']
FILE_ID = '1DXF7Qf6Zjc6yQIboDmqwl3s9l3Y6yKNK'

def download_and_parse_to_json():
    result = {}

    service_builder = GoogleServiceBuilder()
    service = service_builder.build_service(SCOPES, 'drive', 'v3')

    request = service.files().get_media(fileId=FILE_ID)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    
    workbook = openpyxl.load_workbook(fh, data_only=True)
    worksheet = workbook.active

    meetings = []
    students = []

    current_row = 0
    for row in worksheet.values:
        current_student = {}
        current_point_breakdown = []
        current_column = 0
        for value in row:
            if current_row == 0:
                if value and value != "TOTALS":
                    list.append(meetings, value)
            else:
                if current_column == 0:
                    current_student["name"] = value
                elif current_column == len(row) - 1:
                    current_student["pointTotal"] = value
                else:
                    value_to_append = 0
                    if value:
                        value_to_append = value
                    list.append(current_point_breakdown, value_to_append)
            current_column += 1
        current_row += 1
        if len(current_point_breakdown) != 0:
            current_student["pointBreakdown"] = current_point_breakdown
        if current_student:
            list.append(students, current_student)
    
    result["meetings"] = meetings
    result["students"] = sorted(students, key = lambda x: (x['pointTotal'], x['name']), reverse=True)

    return result

