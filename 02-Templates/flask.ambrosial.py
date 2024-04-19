from flask import Flask, render_template, url_for
app = Flask(__name__)

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
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
