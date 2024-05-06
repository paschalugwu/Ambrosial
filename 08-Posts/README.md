# Ambrosial Flask Application

This is a Flask web application named 'Ambrosial'. The application allows users to create an account, log in, create posts, and view posts from other users. The application uses a SQLite database to store user and post data.

## Project Structure

The project structure is as follows:

```
.
├── README.md
├── flask_ambrosial
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   ├── main.css
│   │   ├── post_pics
│   │   └── profile_pics
│   └── templates
│       ├── about.html
│       ├── account.html
│       ├── create_post.html
│       ├── home.html
│       ├── layout.html
│       ├── login.html
│       ├── post.html
│       └── register.html
├── instance
│   └── site.db
├── migrations
│   ├── README
│   ├── __pycache__
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
└── run.py
```

## Application Components

### `flask_ambrosial` Package

This is the main package for the Flask application. It contains the application's Python modules, static files, and templates.

#### `__init__.py`

This file initializes the Flask application and its extensions, such as Flask-SQLAlchemy for the database and Flask-Login for user authentication. It also imports the routes from the `routes.py` module.

#### `forms.py`

This module defines the WTForms form classes for the application. These forms handle user input in the application's routes and templates.

#### `models.py`

This module defines the SQLAlchemy models for the application. These models represent the tables in the application's database.

#### `routes.py`

This module defines the routes for the Flask application. Each route is a function that handles a specific URL pattern. The routes use the forms and models to handle user input and database interactions.

### `static` Directory

This directory contains the static files for the application, such as CSS files and user-uploaded images.

#### `main.css`

This is the main CSS file for the application. It defines the styles for the application's templates.

#### `post_pics` and `profile_pics` Directories

These directories store the user-uploaded images for posts and user profile pictures, respectively.

### `templates` Directory

This directory contains the Jinja2 templates for the application. These templates define the HTML structure of the application's web pages.

#### `layout.html`

This is the base template for the application. It defines the overall structure of the web pages, including the navigation bar and the main content section.

#### `home.html`, `login.html`, `register.html`, etc.

These templates extend the base template and fill in the "content" block with page-specific content.

### `instance` Directory

This directory contains the SQLite database file for the application (`site.db`).

### `migrations` Directory

This directory contains the Alembic migration scripts for the application's database. These scripts handle changes to the database schema.

### `run.py`

This is the main entry point for running the Flask application. It imports the Flask application instance from the `flask_ambrosial` package and runs it.

## Application Behavior

When a user visits the application, they are presented with a list of posts from all users. If the user is not logged in, they can register a new account or log in to an existing account.

Once logged in, the user can create new posts and view their account details. They can also update their account details, including their username, email, and profile picture.

Each post includes the post's author, date posted, title, and content. If the post's author is the current user, they can update or delete the post.

The application uses Flask-Login to handle user sessions, so even if the user closes the application, they will remain logged in until they log out.

The application uses Flask-SQLAlchemy to interact with the SQLite database. All user and post data is stored in the database, and the application queries the database to retrieve this data when needed.

The application uses WTForms for form handling, including user input validation and rendering form fields in templates. The application uses Bootstrap for its styles and layout.

## Conclusion

The Ambrosial Flask application is a robust blogging platform that allows users to share posts and interact with each other. It demonstrates the power and flexibility of Flask and its extensions, including Flask-SQLAlchemy, Flask-Login, and WTForms. With its well-structured code and clear separation of concerns, it serves as a great example of a modern Flask application.
