#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    """
    Form for user registration.

    Attributes:
        username (StringField): Field for entering username.
        email (StringField): Field for entering email.
        password (PasswordField): Field for entering password.
        confirm_password (PasswordField): Field for confirming password.
        submit (SubmitField): Button for submitting registration form.
    """
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    """
    Form for user login.

    Attributes:
        email (StringField): Field for entering email.
        password (PasswordField): Field for entering password.
        remember (BooleanField): Checkbox for remembering user login.
        submit (SubmitField): Button for submitting login form.
    """
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
