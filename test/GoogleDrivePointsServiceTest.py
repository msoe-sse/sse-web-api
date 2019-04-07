import unittest
from app.GoogleDrivePointsService import GoogleDrivePointsService

class GoogleDrivePointsServiceTest(unittest.TestCase):
    def test_parse_meetings(self):
        #Arrange
        cell_values = [[self.MockCell(None), self.MockCell("General Meeting 1"), 
                        self.MockCell("General Meeting 2"), self.MockCell("General Meeting 3")]]

        service = GoogleDrivePointsService()

        #Act
        result = service._parse_meetings(cell_values)

        #Assert
        self.assertCountEqual(["General Meeting 1", "General Meeting 2", "General Meeting 3"], result)
    
    def test_parse_students_basic(self):
        #Arrange
        cell_values = [[self.MockCell("Student 1"), self.MockCell(1), self.MockCell(1), 
                        self.MockCell(1), self.MockCell(3)]]

        service = GoogleDrivePointsService()

        #Act
        result = service._parse_students(cell_values)

        #Assert
        self.assertEqual(1, len(result))
        self._assert_student("Student 1", [1, 1, 1], 3, result[0])

    def test_parse_student_sorting(self):
        #Arrange
        cell_values = [[self.MockCell("Student 1"), self.MockCell(1), self.MockCell(1), self.MockCell(None), self.MockCell(2)],
                       [self.MockCell("Student 2"), self.MockCell(1), self.MockCell(None), self.MockCell(None), self.MockCell(1)],
                       [self.MockCell("Student 3"), self.MockCell(1), self.MockCell(1), self.MockCell(1), self.MockCell(3)]]
        
        service = GoogleDrivePointsService()

        #Act
        result = service._parse_students(cell_values)

        #Assert
        self.assertEqual(3, len(result))
        self._assert_student("Student 3", [1, 1, 1], 3, result[0])
        self._assert_student("Student 1", [1, 1, 0], 2, result[1])
        self._assert_student("Student 2", [1, 0, 0], 1, result[2])

    def _assert_student(self, name, point_breakdown, point_total, student):
        self.assertEqual(name, student["name"])
        self.assertCountEqual(point_breakdown, student["pointBreakdown"])
        self.assertEqual(point_total, student["pointTotal"])

    class MockCell():
        def __init__(self, value):
            self.value = value

if __name__ == '__main__':
    unittest.main()