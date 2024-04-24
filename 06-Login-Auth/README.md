# Ambrosial - Login Authentication Flask App

## Overview
This Flask web application, named Ambrosial, provides a platform for users to register, log in, log out, and view personalized account information. It includes user authentication, password hashing, and basic CRUD (Create, Read, Update, Delete) functionalities.

## Project Structure
```
.
├── README.md
├── flask_ambrosial
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   └── main.css
│   └── templates
│       ├── about.html
│       ├── account.html
│       ├── home.html
│       ├── layout.html
│       ├── login.html
│       └── register.html
├── instance
│   └── site.db
└── run.py
```

## Setup and Usage
1. **Environment Setup**
   - Clone the repository.
   - Create and activate a virtual environment:
     ```
     python3 -m venv venv
     source venv/bin/activate  # For Linux/Mac
     venv\Scripts\activate      # For Windows
     ```
   - Install the required dependencies:
     ```
     pip install -r requirements.txt
     ```

2. **Database Setup**
   - The SQLite database is used (`instance/site.db`).
   - Initialize the database:
     ```
     flask db init
     flask db migrate -m "Initial migration"
     flask db upgrade
     ```

3. **Running the App**
   - Start the Flask server:
     ```
     python run.py
     ```
   - The app will be accessible at `http://localhost:5000/`.

## Functionality
- **Register**
  - New users can create an account with a unique username and email.
  - Passwords are securely hashed before storing in the database.
  - Validation ensures no duplicate usernames or emails.
  - Upon successful registration, users are redirected to the login page.

- **Login**
  - Existing users can log in with their registered email and password.
  - Passwords are checked against the hashed versions in the database.
  - Remember Me option allows persistent login across sessions.
  - Invalid login attempts display appropriate error messages.

- **Logout**
  - Logged-in users can log out, terminating their session.
  - Upon logout, users are redirected to the home page.

- **User Account**
  - Authenticated users can view their account details.
  - The account page displays the username of the logged-in user.
  - Non-authenticated users are redirected to the login page.

- **Home and About Pages**
  - The home page (`/home`) displays a list of posts.
  - Each post includes the author, title, content, and date posted.
  - The about page (`/about`) provides information about the Ambrosial app.

## File Descriptions
- **run.py**
  - Entry point of the application, runs the Flask app.

- **flask_ambrosial**
  - **\_\_init\_\_.py**
    - Initializes the Flask app, configures extensions.
  - **forms.py**
    - Defines WTForms for user registration and login.
  - **models.py**
    - Defines database models for User and Post.
  - **routes.py**
    - Contains route definitions for the application.
  - **static/main.css**
    - CSS file for styling the templates.
  - **templates/**
    - Contains HTML templates for different pages.

## Dependencies
- Flask: Micro web framework for Python.
- Flask-WTF: Simple integration of WTForms with Flask.
- Flask-SQLAlchemy: Flask extension for SQLAlchemy, ORM tool.
- Flask-Bcrypt: Flask extension for password hashing.
- Flask-Login: Flask extension for managing user authentication.
