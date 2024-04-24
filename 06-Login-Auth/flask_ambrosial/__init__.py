#!/usr/bin/env python3
"""Initialization of the Flask application and its extensions."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initialize the Flask application
app = Flask(__name__)

# Secret key for securing the session
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# Database configuration
# Using SQLite for this example, 'site.db' will be created in the current directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Create an SQLAlchemy database instance
db = SQLAlchemy(app)

# Create a Bcrypt instance for password hashing
bcrypt = Bcrypt(app)

# Create a LoginManager instance for managing user sessions
login_manager = LoginManager(app)

# Configure the login view for redirecting unauthorized users
login_manager.login_view = 'login'

# Configure the message category for flashing messages
login_manager.login_message_category = 'info'

# Import routes module to ensure routes are registered
from flask_ambrosial import routes

# Note: The routes module must be imported after creating the Flask app
# This is to avoid circular imports, as routes might need to import things from this file
# By importing routes after creating the app, the app instance is already defined
# and can be used in the routes module for defining the routes and their functionalities
