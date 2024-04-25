#!/usr/bin/env python3
from flask import Flask, render_template, url_for, flash, redirect
# Importing form classes from forms.py
from forms import RegistrationForm, LoginForm
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # Creating a Flask application instance
# Secret key for CSRF protection
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Database URI
# Creating a SQLAlchemy instance bound to the Flask application
db = SQLAlchemy(app)


class User(db.Model):
    """
    Model class for the User table in the database.

    Attributes:
    - id: Primary key of the user
    - username: Username of the user (unique, not nullable)
    - email: Email address of the user (unique, not nullable)
    - image_file: File name of the user's profile image \
        (nullable, default='default.jpg')
    - password: Password of the user (not nullable)
    - posts: Relationship to the Post model (one-to-many)
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        """Representation of a User object."""
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    """
    Model class for the Post table in the database.

    Attributes:
    - id: Primary key of the post
    - title: Title of the post (not nullable)
    - date_posted: Date and time when the post was \
        created (not nullable, default=datetime.now(timezone.utc))
    - content: Content of the post (not nullable)
    - user_id: Foreign key referencing the id of the User \
        who created the post (not nullable)
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime,
                            nullable=False, default=datetime.now(timezone.utc))
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """Representation of a Post object."""
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        'author': 'Ugwu Paschal',
        'title': 'How to prepare Jollof Rice.',
        'content': 'Jollof rice, a beloved West African dish, \
            is a flavorful one-pot meal. Made from rice, tomatoes, \
                onions, peppers, and aromatic spices, it’s a \
                    staple during holidays, weddings, and \
                        special events. Customize it with your \
                            favorite veggies and pair it with fried \
                                plantains for a delightful feast!',
        'date_posted': 'April 18, 2024'
    },
    {
        'author': 'Amarachi Nnanta',
        'title': 'Prepare Egusi Soup Like A Pro.',
        'content': 'Egusi soup, a Nigerian delicacy, \
            is rich and flavorful. To prepare it like \
                a pro, heat oil in a pot and sauté onions. \
                    Add ingredients (except ground egusi) and \
                        boil for 3 minutes. Stir in ground \
                            egusi, adjusting water for desired \
                                consistency. Cook on low heat \
                                    for 15-20 minutes, and serve with \
                                        yam, rice, or grilled meat.',
        'date_posted': 'April 19, 2024'
    }
]


@app.route("/")
@app.route("/home")
def home():
    """Route function for the home page."""
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    """Route function for the about page."""
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    """Route function for user registration."""
    form = RegistrationForm()  # Creating an instance of the RegistrationForm
    if form.validate_on_submit():
        # Flashing a success message
        flash(f'Account created for \
              {form.username.data}!', 'success')
        return redirect(url_for('home'))  # Redirecting to the home page
    # Rendering the register.html template
    return render_template('register.html',
                           title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """Route function for user login."""
    form = LoginForm()  # Creating an instance of the LoginForm
    if form.validate_on_submit():
        if form.email.data == 'ugwupaschal@gmail.com' \
                and form.password.data == 'paschal':
            # Flashing a success message
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))  # Redirecting to the home page
        else:
            # Flashing a danger message
            flash('Login Unsuccessful. \
                Please check username and password', 'danger')
    # Rendering the login.html template
    return render_template('login.html',
                           title='Login', form=form)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creating all tables in the database
    app.run(debug=True)  # Running the Flask application in debug mode
