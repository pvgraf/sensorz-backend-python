"""
WSGI File

This file contains the WSGI application entry point.
"""

from app import app, db
from routes import *

# Ensure the database tables are created within the app context
with app.app_context():
    db.create_all()

# Run the Flask app if this file is executed directly
if __name__ == "__main__":
    app.run()
