#!/usr/bin/env python3

# Import necessary modules and objects from the Flask app
from flask import render_template, url_for, flash, redirect
from flask_ambrosial import app
from flask_ambrosial.forms import RegistrationForm, LoginForm

# Dummy posts data for demonstration purposes
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
        'content': 'Egusi soup, a Nigerian delicacy, is rich \
            and flavorful. To prepare it like a pro, heat oil \
                in a pot and sauté onions. Add ingredients \
                    (except ground egusi) and boil for \
                        3 minutes. Stir in ground egusi, \
                            adjusting water for desired \
                                consistency. Cook on low heat \
                                    for 15-20 minutes, and serve\
                                        with yam, rice, or \
                                            grilled meat.',
        'date_posted': 'April 19, 2024'
    }
]


# Route for the home page
@app.route("/")
@app.route("/home")
def home():
    """
    Route for the home page.

    Returns:
        render_template: Renders the home.html template with posts data.
    """
    return render_template('home.html', posts=posts)


# Route for the about page
@app.route("/about")
def about():
    """
    Route for the about page.

    Returns:
        render_template: Renders the about.html template with a title.
    """
    return render_template('about.html', title='About')


# Route for user registration
@app.route("/register", methods=['GET', 'POST'])
def register():
    """
    Route for user registration.

    Returns:
        render_template: Renders the register.html template \
            with a registration form.
        redirect: Redirects to the home page upon successful registration.
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


# Route for user login
@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    Route for user login.

    Returns:
        render_template: Renders the login.html template with a login form.
        redirect: Redirects to the home page upon successful login.
    """
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ugwupaschal@gmail.com' \
                and form.password.data == 'paschal':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. \
                Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
