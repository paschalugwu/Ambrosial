## Ambrosial

### Package Structure

```plaintext
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
│       ├── home.html
│       ├── layout.html
│       ├── login.html
│       └── register.html
├── instance
└── run.py
```

### Overview

Ambrosial is a Flask application designed to provide users with a platform to share and discover culinary tips, recipes, and techniques. Users can register, log in, and browse through posts submitted by other users. The application features a clean and intuitive user interface built with HTML, CSS, and Bootstrap.

### Functionalities

- **User Authentication**: Users can register for an account and log in securely.
- **Post Display**: Home page displays posts submitted by users, including author, title, content, and posting date.
- **About Page**: Provides information about the application.
- **Registration**: Users can sign up for an account with a unique username, email, and password.
- **Login**: Registered users can log in to their accounts securely.
- **Flash Messages**: Users receive feedback messages for successful or unsuccessful actions.

### Code Structure

- **`flask_ambrosial` Package**:
  - **`__init__.py`**: Initializes the Flask application and sets up database configuration.
  - **`forms.py`**: Defines forms for user registration and login using Flask-WTF.
  - **`models.py`**: Contains SQLAlchemy models for User and Post, defining database schema.
  - **`routes.py`**: Defines routes and view functions for handling user requests.
  - **`static` Directory**: Contains CSS files for styling.
  - **`templates` Directory**: Contains HTML templates for rendering pages.
- **`instance` Directory**: Placeholder for configuration files.
- **`run.py`**: Entry point to run the Flask application.

### How to Run

1. Install dependencies using `pip install -r requirements.txt`.
2. Set up the Flask application by running `export FLASK_APP=run.py`.
3. Initialize the database with `flask db init`.
4. Run the application with `flask run`.

### Dependencies

- Flask
- Flask-WTF
- Flask-SQLAlchemy

### Contributors

- Ugwu Paschal

### License

This project is licensed under the MIT License.
