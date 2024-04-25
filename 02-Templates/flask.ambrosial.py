#!/usr/bin/env python3
from flask import Flask, render_template, url_for

# Initialize Flask app
app = Flask(__name__)

# Sample data of posts
posts = [
    {
        'author': 'Ugwu Paschal',
        'title': 'How Jellof-Rice Is Prepared.',
        'content': 'First post content',
        'date_posted': 'April 18, 2024'
    },
    {
        'author': 'Amarachi Nnanta',
        'title': 'Prepare Egusi Soup Like A Pro.',
        'content': 'Second post content',
        'date_posted': 'April 19, 2024'
    }
]


@app.route("/")
@app.route("/home")
def home():
    """
    Route handler for the home page.

    Returns:
        Rendered HTML template (home.html) with posts data passed as context.
    """
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    """
    Route handler for the about page.

    Returns:
        Rendered HTML template (about.html) with title passed as context.
    """
    return render_template('about.html', title='About')


if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
