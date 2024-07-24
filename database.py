"""
Database Module

This module contains the FDataBase class for interacting with the database.
"""

import statistics
from models import User


class FDataBase:
    """
    FDataBase Class

    Provides methods for adding, retrieving, and performing statistics on grades in the database.
    """
    def __init__(self, db):
        self.__db = db

    def add_data(self, student_name, math_grade, science_grade, history_grade):
        """
        Add data to the database.

        Args:
            student_name (str): Name of the student.
            math_grade (int): Math grade of the student.
            science_grade (int): Science grade of the student.
            history_grade (int): History grade of the student.

        Returns:
            bool: True if the data was added successfully, False otherwise.
        Note:
            Validation defined at the HTML level (grade (0-100), required fields etc.)
        """
        try:
            user = User.query.filter_by(username=student_name).first()
            if user:
                user.math_grade = math_grade
                user.science_grade = science_grade
                user.history_grade = history_grade
            else:
                user = User(
                    username=student_name,
                    math_grade=math_grade,
                    science_grade=science_grade,
                    history_grade=history_grade,
                )
                self.__db.session.add(user)
            self.__db.session.commit()
            return True
        except Exception as err: # pylint: disable=W0718
            print("An unexpected error occurred during the execution.", err)
            return False

    def get_grade_by_id(self, student_id):
        """
        Get grades by student ID from the database.

        Args:
            student_id (int): ID of the student.

        Returns:
            dict: Dictionary containing the student's grades if found, None otherwise.
        """
        try:
            user = User.query.get(student_id)
            if user:
                return {
                    "student_id": user.id,
                    "student_name": user.username,
                    "math_grade": user.math_grade,
                    "science_grade": user.science_grade,
                    "history_grade": user.history_grade,
                }
        except Exception as err: # pylint: disable=W0718
            print("An unexpected error occurred during the execution.", err)
        return None

    def get_subject_stats(self, subject):
        """
        Get statistics by subject from the database.

        Args:
            subject (str): The subject for which statistics are requested.

        Returns:
            dict: Dictionary containing statistics for the specified subject,
                  or None if an error occurs.
        """
        try:
            grades = self.__db.session.query(getattr(User, subject)).all()
            num_students = len(grades)
            if num_students > 0:
                grade_values = [grade[0] for grade in grades]
                average_grade = sum(grade_values) / num_students
                median_grade = statistics.median(grade_values)
                return {
                    "subject": subject,
                    "num_students": num_students,
                    "average_grade": average_grade,
                    "median_grade": median_grade,
                }
        except Exception as err: # pylint: disable=W0718
            print("An unexpected error occurred during the execution.", err)
        return None
