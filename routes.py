"""
Routes Module

This module contains Flask routes for managing grades in the database.
"""

from flask import render_template, request, flash
from app import app
from models import db
from database import FDataBase

# Creating an instance of the FDataBase class
dbase = FDataBase(db)


# Route for adding grades
@app.route("/add-grades", methods=["POST", "GET"])
def add_grades():
    """Route for adding grades to the database."""
    if request.method == "POST":
        # Adding data to the database upon form submission
        res = dbase.add_data(
            request.form["student_name"],
            request.form["math_grade"],
            request.form["science_grade"],
            request.form["history_grade"],
        )

        # Checking the result and displaying a message with flash msg
        if not res:
            flash("Error occurred while attempting to add to the DB.")
        else:
            flash("Successfully added to the DB")

    # Displaying the add_grades.html template
    return render_template("add_grades.html")


# Route for getting grades by student ID
@app.route("/grades-by-student/<student_id>", methods=["GET"])
def get_grades_by_student(student_id):
    """Route for getting grades by student ID from the database."""
    # Getting grades from the database by ID
    data = dbase.get_grade_by_id(student_id)

    if data:
        # Calculating the average grade
        data["average_grade"] = (
            data["math_grade"] + data["science_grade"] + data["history_grade"]
        ) / 3

    # Displaying the student_grades.html template with the data
    return render_template(
        "student_grades.html", data=data, error="Incorrect student ID!"
    )


# Route for getting grades by subject
@app.route("/grades-by-subject/<subject>", methods=["GET"])
def get_grades_by_subject(subject):
    """Route for getting statistics by subject from the database."""
    # Getting statistics by subject from the database
    data = dbase.get_subject_stats(f"{subject}_grade")

    # Displaying the get_subject_stats.html template with the data
    return render_template(
        "get_subject_stats.html", subject=subject, data=data, error="Incorrect subject!"
    )
