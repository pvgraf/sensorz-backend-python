"""
app.py

This module initializes a Flask application, sets up database configurations,
and runs the application.
"""

from os import path
from flask import Flask
from models import db

# Create a Flask application
app = Flask(__name__)

# Set the SQLALCHEMY_DATABASE_URI to use a SQLite database located at /app/data/grades.db
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f'sqlite:///{path.join("/app/data", "grades.db")}'
)

# Disable tracking modifications to avoid unnecessary overhead
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Set a secret key for the application
app.config["SECRET_KEY"] = "kjhgbjhgkb%&^%jhknjhnkjhny65"

# Initialize the database with the Flask application
db.init_app(app)

# Run the Flask app if this file is executed directly
if __name__ == "__main__":
    # Importing route definitions at the end to avoid circular imports
    from routes import *

    # Create all database tables within the application context
    with app.app_context():
        db.create_all()

    # Run the Flask application with debugging enabled
    app.run(host="0.0.0.0", port=5050, debug=True)
