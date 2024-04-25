#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    """
    Form class for user registration.

    Fields:
    - username: StringField for username (required, \
        length between 2 and 20 characters)
    - email: StringField for email (required, valid email format)
    - password: PasswordField for password (required)
    - confirm_password: PasswordField for confirming \
        password (required, must match 'password' field)
    - submit: SubmitField for submitting the form
    """
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    """
    Form class for user login.

    Fields:
    - email: StringField for email (required, valid email format)
    - password: PasswordField for password (required)
    - remember: BooleanField for remembering user session
    - submit: SubmitField for submitting the form
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
