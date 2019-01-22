import os
import json
import google.auth
from googleapiclient.discovery import build
from google.oauth2 import service_account
from app.GoogleServiceBuilder import GoogleServiceBuilder
from collections import deque

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = '1EkZkQogMIfVETUQUzkwoPPfGKF6kjhVhuWsp4EuYDTc'

class GoogleSheetsService():
    def __init__(self):
        self.sheets_service = self._build_sheets_service()

    def get_point_data(self):
        parsed_result = {}

        first_row_result = self._parse_first_row()
        parsed_result['meetings'] = first_row_result[0]
        parsed_result['students'] = self._parse_students(first_row_result[1])

        return parsed_result

    def _build_sheets_service(self):
        service_builder = GoogleServiceBuilder()
        return service_builder.build_service(SCOPES, 'sheets', 'v4')

    def _get_cells(self, range):
        sheet = self.sheets_service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=range).execute()
        values = result.get('values', [])
        return values

    def _parse_first_row(self):
        meetings = []
        current_column = 'A'

        first_row_range = 'Sheet1!A1:Z1'
        first_row_cells = self._get_cells(first_row_range)[0]
        cell_queue = deque(first_row_cells)

        current_value = cell_queue.popleft()
        while current_value != 'TOTALS' and len(cell_queue) != 0:
            current_column = chr(ord(current_column) + 1)
            if current_value != "": meetings.append(current_value)
            current_value = cell_queue.popleft()

        return meetings, current_column
    
    def _parse_students(self, last_column):
        students = []
        current_row = 2
        current_cells = self._get_cells_from_row(current_row, last_column)
        while current_cells:
            students.append(self._parse_student(current_cells))
            current_row += 1
            current_cells = self._get_cells_from_row(current_row, last_column)
        return sorted(students, key = lambda x: (x['pointTotal'], x['name']), reverse=True)

    def _parse_student(self, current_cells):
        current_student = {}
        current_student['name'] = current_cells[0][0]
        current_student['pointTotal'] = int(current_cells[0][-1])
        current_student['pointBreakdown'] = self._parse_point_breakdown(current_cells)
        return current_student

    def _parse_point_breakdown(self, current_cells):
        result = []
        for i in range(1, len(current_cells[0]) - 2):
            value_to_append = current_cells[0][i]
            if value_to_append == "":
                value_to_append = 0
            else:
                value_to_append = int(value_to_append)
            result.append(value_to_append)
        return result

    def _get_cells_from_row(self, current_row, last_column):
        current_range = 'Sheet1!A{}:{}{}'.format(current_row, last_column, current_row)
        current_cells  = self._get_cells(current_range)
        return current_cells

