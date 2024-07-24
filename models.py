"""
Models Module

This module contains the database models for the application.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """
    User Model

    Represents a user with associated grades in the database.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    math_grade = db.Column(db.Integer, nullable=False)
    science_grade = db.Column(db.Integer, nullable=False)
    history_grade = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
