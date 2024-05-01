#!/usr/bin/python3
"""Forms for user registration and login."""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, \
    Length, Email, EqualTo, ValidationError
from flask_ambrosial.models import User


class RegistrationForm(FlaskForm):
    """Form for user registration."""

    # Fields for username, email, password, and confirm password
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """Validation to check if username is already taken."""
        # Query the database for a user with the same username
        user = User.query.filter_by(username=username.data).first()
        if user:
            # If a user with this username exists, raise a validation error
            raise ValidationError('That username is taken. \
                Please choose a different one.')

    def validate_email(self, email):
        """Validation to check if email is already registered."""
        # Query the database for a user with the same email
        user = User.query.filter_by(email=email.data).first()
        if user:
            # If a user with this email exists, raise a validation error
            raise ValidationError('That email is taken. \
                Please choose a different one.')


class LoginForm(FlaskForm):
    """Form for user login."""

    # Fields for email, password, remember me checkbox, and submit button
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
