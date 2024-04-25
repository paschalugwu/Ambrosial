#!/usr/bin/env python3

# Import necessary modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)

# Set Flask app configurations
# - SECRET_KEY is used to keep data secure (e.g., for form submissions)
# - SQLALCHEMY_DATABASE_URI specifies the location of the SQLite database file
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Create a SQLAlchemy database instance, linking it to the Flask app
db = SQLAlchemy(app)

# Import routes from the flask_ambrosial package
# This imports routes and registers them with the Flask app
from flask_ambrosial import routes
