import os
import json
from app.GoogleServiceBuilder import GoogleServiceBuilder
import pygsheets

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

class GoogleSheetsService():

    def get_point_data(self):
        parsed_result = {}

        worksheet = self.gc.open_by_key(os.environ.get('GOOGLE_FILE_ID')).sheet1
        cell_values = worksheet.get_all_values()

        first_row_result = self._parse_first_row(cell_values)
        parsed_result['meetings'] = first_row_result
        parsed_result['students'] = self._parse_students(cell_values, parsed_result['meetings'])

        return parsed_result


    def _setup_pygsheets(self):
        service_builder = GoogleServiceBuilder()
        credentials = service_builder.build_credentials(SCOPES)
        self.gc = pygsheets.authorize(custom_credentials=credentials)

    def _parse_first_row(self, cell_values):
        meetings = []
        first_row = cell_values[0]
        for value in first_row:
            if value != "":
                meetings.append(value)
        del meetings[-1]
        return meetings

    def _parse_students(self, cell_values, meetings):
        students = []
        for i in range(1, len(cell_values)):
            current_student = self._parse_student(cell_values[i], meetings)
            if len(current_student) != 0:
                students.append(current_student)
        return sorted(students, key = lambda x: (x['pointTotal'], x['name']), reverse=True)

    def _parse_student(self, current_row, meetings):
        current_student = {}
        if current_row[0] != "":
            current_student['name'] = current_row[0]
            current_student['pointTotal'] = int(current_row[len(meetings) + 1])
            current_student['pointBreakdown'] = self._parse_point_breakdown(current_row, meetings)
        return current_student

    def _parse_point_breakdown(self, current_row, meetings):
        result = []
        for i in range(1, len(meetings) + 1):
            value_to_append = current_row[i]
            if value_to_append == "":
                value_to_append = 0
            else:
                value_to_append = int(value_to_append)
            result.append(value_to_append)
        return result

