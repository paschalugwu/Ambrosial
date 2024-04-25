#!/usr/bin/env python3
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# Initialize Flask app
app = Flask(__name__)
# Set a secret key for session management (required by Flask-WTF)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# Sample posts data
posts = [
    {
        'author': 'Ugwu Paschal',
        'title': 'How to prepare Jollof Rice.',
        'content': 'Jollof rice, a beloved West African dish, \
            is a flavorful one-pot meal. Made from rice, \
                tomatoes, onions, peppers, and aromatic \
                    spices, it’s a staple during holidays, \
                        weddings, and special events. Customize \
                            it with your favorite veggies and \
                                pair it with fried plantains \
                                    for a delightful feast!',
        'date_posted': 'April 18, 2024'
    },
    {
        'author': 'Amarachi Nnanta',
        'title': 'Prepare Egusi Soup Like A Pro.',
        'content': 'Egusi soup, a Nigerian delicacy, \
            is rich and flavorful. To prepare it like \
                a pro, heat oil in a pot and sauté onions. \
                    Add ingredients (except ground egusi) \
                        and boil for 3 minutes. Stir in \
                            ground egusi, adjusting water \
                                for desired consistency. \
                                    Cook on low heat for \
                                        15-20 minutes, \
                                            and serve \
                                                with yam, \
                                                    rice, or \
                                                        grilled meat.',
        'date_posted': 'April 19, 2024'
    }
]


@app.route("/")
@app.route("/home")
def home():
    """Route: Home Page"""
    # Render home page template with posts data
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    """Route: About Page"""
    # Render about page template
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    """Route: Registration Page"""
    # Create registration form instance
    form = RegistrationForm()
    # If form is submitted and valid
    if form.validate_on_submit():
        # Flash success message and redirect to home page
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    # Render registration template with form
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """Route: Login Page"""
    # Create login form instance
    form = LoginForm()
    # If form is submitted and valid
    if form.validate_on_submit():
        # Check if credentials match (dummy check)
        if form.email.data == 'ugwupaschal@gmail.com' \
                and form.password.data == 'paschal':
            # Flash success message and redirect to home page
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            # Flash error message for unsuccessful login
            flash('Login Unsuccessful. \
                Please check username and password', 'danger')
    # Render login template with form
    return render_template('login.html', title='Login', form=form)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
