#!/usr/bin/env python3
"""Routes and views for the Flask app."""

from flask import render_template, url_for, flash, redirect, request
from flask_ambrosial import app, db, bcrypt
from flask_ambrosial.forms import RegistrationForm, LoginForm
from flask_ambrosial.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

# Sample posts data (temporary)
posts = [
    {
        'author': 'Ugwu Paschal',
        'title': 'How to prepare Jollof Rice.',
        'content': 'Jollof rice, a beloved West African dish, \
            is a flavorful one-pot meal. Made from rice, \
                tomatoes, onions, peppers, and aromatic spices, \
                    it’s a staple during holidays, weddings, \
                        and special events. Customize it with \
                            your favorite veggies and pair it \
                                with fried plantains for a \
                                    delightful feast!',
        'date_posted': 'April 18, 2024'
    },
    {
        'author': 'Amarachi Nnanta',
        'title': 'Prepare Egusi Soup Like A Pro.',
        'content': 'Egusi soup, a Nigerian delicacy, \
            is rich and flavorful. To prepare it like a pro, \
                heat oil in a pot and sauté onions. Add \
                    ingredients (except ground egusi) and boil \
                        for 3 minutes. Stir in ground egusi, \
                            adjusting water for desired \
                                consistency. Cook on low heat \
                                    for 15-20 minutes, and \
                                        serve with yam, rice, \
                                            or grilled meat.',
        'date_posted': 'April 19, 2024'
    }
]


@app.route("/")
@app.route("/home")
def home():
    """Render the home page with posts."""
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    """Render the about page."""
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Hash the password before storing it
        hashed_password = bcrypt.generate_password_hash(form.password.data)\
            .decode('utf-8')
        # Create a new User object
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        # Add the user to the database session
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! \
            You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # Check if the user exists and the password is correct
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            # Log in the user
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else \
                redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. \
                Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    """Handle user logout."""
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    """Render the user's account page."""
    return render_template('account.html', title='Account')
