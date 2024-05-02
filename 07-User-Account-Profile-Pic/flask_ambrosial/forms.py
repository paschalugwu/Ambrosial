#!/usr/bin/python3
"""Forms for user registration, login, and account update."""

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_ambrosial.models import User

class RegistrationForm(FlaskForm):
    """Form for user registration."""

    def validate_username(self, username):
        """
        Validate if the username is already taken.

        Args:
            username (str): The username entered by the user.

        Raises:
            ValidationError: If a user with the same username already exists.
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. \
                Please choose a different one.')

    def validate_email(self, email):
        """
        Validate if the email is already registered.

        Args:
            email (str): The email entered by the user.

        Raises:
            ValidationError: If a user with the same email already exists.
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. \
                Please choose a different one.')

class LoginForm(FlaskForm):
    """Form for user login."""

class UpdateAccountForm(FlaskForm):
    """Form for updating user account."""

    def validate_username(self, username):
        """
        Validate if the username is already taken during account update.

        Args:
            username (str): The username entered by the user.

        Raises:
            ValidationError: If a user with the same username already exists.
        """
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. \
                    Please choose a different one.')

    def validate_email(self, email):
        """
        Validate if the email is already registered during account update.

        Args:
            email (str): The email entered by the user.

        Raises:
            ValidationError: If a user with the same email already exists.
        """
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. \
                    Please choose a different one.')
