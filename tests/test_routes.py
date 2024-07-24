"""
Module for testing the routes of the Flask application.
"""

import unittest
import requests


class TestAppRoutes(unittest.TestCase):
    """
    Test case for verifying the functionality of the application routes.
    """

    BASE_URL = "http://127.0.0.1:5050"
    TIMEOUT = 10

    def test_grades_by_student_page(self):
        """
        Test case to check if the student grades page is rendered correctly.
        """
        _id = 1
        response = requests.get(
            f"{self.BASE_URL}/grades-by-student/{_id}", timeout=self.TIMEOUT
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Student Grades Information", response.text)
        self.assertIn(f"Student ID: {_id}", response.text)

    def test_grades_by_subject_page(self):
        """
        Test case to check if the grades by subject pages are rendered correctly.
        """
        for subject in ["math", "history", "science"]:
            response = requests.get(
                f"{self.BASE_URL}/grades-by-subject/{subject}", timeout=self.TIMEOUT
            )
            self.assertEqual(response.status_code, 200)
            if subject == "math":
                self.assertIn("Statistics for math", response.text)
            elif subject == "history":
                self.assertIn("Statistics for history", response.text)
            elif subject == "science":
                self.assertIn("Statistics for science", response.text)
            self.assertIn("Average Grade", response.text)


if __name__ == "__main__":
    unittest.main()
