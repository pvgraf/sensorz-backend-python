# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Required for uWSGI installation
RUN apt-get update && apt-get install -y build-essential

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Open port 5050 for the Flask app
EXPOSE 5050

# Define a volume for the application data
VOLUME /app/data

# Define the command to run the application using uWSGI
CMD ["/bin/sh", "-c", "uwsgi --socket 0.0.0.0:5050 --protocol=http -w wsgi --ini uwsgi.ini"]
