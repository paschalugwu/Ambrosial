# Ambrosial

Ambrosial is a web application built with Flask, a lightweight Python web framework. It allows users to register, log in, and view posts about cooking recipes. The application utilizes SQLAlchemy for database management and WTForms for form validation.

.
├── README.md
├── flask_ambrosial.py
├── forms.py
├── instance
│   └── site.db
├── interact_guide.md
├── static
│   └── main.css
└── templates
    ├── about.html
    ├── home.html
    ├── layout.html
    ├── login.html
    └── register.html

## Functionality

- **Registration**: Users can create an account by providing a username, email, and password. Upon successful registration, users receive a confirmation message and are redirected to the home page.

- **Login**: Registered users can log in using their email and password. Upon successful login, users receive a confirmation message and are redirected to the home page.

- **Home Page**: The home page displays a list of cooking recipe posts. Each post includes the author's name, title, content, and date posted.

- **About Page**: The about page provides information about the Ambrosial web application.

## File Structure

- **flask_ambrosial.py**: Contains the main Flask application code, including route definitions, database models, and form handling.

- **forms.py**: Defines Flask-WTF forms for user registration and login.

- **instance/site.db**: SQLite database file where user and post data is stored.

- **static/main.css**: CSS stylesheet for styling the web application.

- **templates/**:
  - **about.html**: HTML template for the about page.
  - **home.html**: HTML template for the home page, displaying posts.
  - **layout.html**: Base HTML template containing the overall structure of the application layout.
  - **login.html**: HTML template for the login page.
  - **register.html**: HTML template for the registration page.

## Interactions

- **flask_ambrosial.py**: This file contains the main Flask application code, defining routes for the home page, about page, user registration, and login. It also defines SQLAlchemy database models for users and posts.

- **forms.py**: Defines Flask-WTF forms for user registration and login, including validation logic for username, email, and password fields.

- **instance/site.db**: SQLite database file where user and post data is stored. The database schema is defined by the SQLAlchemy models in flask_ambrosial.py.

- **static/main.css**: CSS stylesheet for styling the web application, providing a visually appealing interface.

- **templates/**: Contains HTML templates for different pages of the web application, including the home page, about page, registration page, and login page.

## Behaviors

- When a user visits the home page ("/"), they can see a list of cooking recipe posts.
- Users can navigate to the about page ("/about") to learn more about the Ambrosial web application.
- New users can register for an account by visiting the registration page ("/register"). After successful registration, they are redirected to the home page.
- Registered users can log in using their credentials on the login page ("/login"). After successful login, they are redirected to the home page.
- Upon successful login or registration, users receive a confirmation message displayed using flash messages.
