#!/usr/bin/env python3
from flask import render_template, url_for, flash, redirect
from flask_ambrosial import app
from flask_ambrosial.forms import RegistrationForm, LoginForm
from flask_ambrosial.models import User, Post

posts = [
    {
        'author': 'Ugwu Paschal',
        'title': 'How to prepare Jollof Rice.',
        'content': 'Jollof rice, a beloved West African dish, is a flavorful one-pot meal. Made from rice, tomatoes, onions, peppers, and aromatic spices, it’s a staple during holidays, weddings, and special events. Customize it with your favorite veggies and pair it with fried plantains for a delightful feast!',
        'date_posted': 'April 18, 2024'
    },
    {
        'author': 'Amarachi Nnanta',
        'title': 'Prepare Egusi Soup Like A Pro.',
        'content': 'Egusi soup, a Nigerian delicacy, is rich and flavorful. To prepare it like a pro, heat oil in a pot and sauté onions. Add ingredients (except ground egusi) and boil for 3 minutes. Stir in ground egusi, adjusting water for desired consistency. Cook on low heat for 15-20 minutes, and serve with yam, rice, or grilled meat.',
        'date_posted': 'April 19, 2024'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ugwupaschal@gmail.com' and form.password.data == 'paschal':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
