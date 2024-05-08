#!/usr/bin/env python3
"""Initialization of the Flask application and its extensions."""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail

# Initialize the Flask application
app = Flask(__name__)

# Secret key for securing the session
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# Database configuration
# Using SQLite for this example, 'site.db' \
# will be created in the current directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Create an SQLAlchemy database instance
db = SQLAlchemy(app)

# initialize Flask-Migrate
migrate = Migrate(app, db)

# Create a Bcrypt instance for password hashing
bcrypt = Bcrypt(app)

# Create a LoginManager instance for managing user sessions
login_manager = LoginManager(app)

# Configure the login view for redirecting unauthorized users
login_manager.login_view = 'login'

# Configure the message category for flashing messages
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

# Import routes module to ensure routes are registered
from flask_ambrosial import routes
