# Ambrosial

Ambrosial is a Flask web application for sharing cooking recipes and tips. It allows users to register, log in, and view various recipes posted by members of the community. Users can also create their own posts with recipes, tips, and tricks for others to discover.

## Project Structure

```
.
├── README.md
├── flask_ambrosial
│   ├── __init__.py
│   ├── forms.py
│   ├── instance
│   │   └── site.db
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
└── run.py
```

### Files and Directories

- **flask_ambrosial/**
  - **\_\_init\_\_.py:** Initializes the Flask application, configures the app, and sets up the database.
  - **forms.py:** Contains the FlaskForm classes for user registration and login.
  - **models.py:** Defines the SQLAlchemy models for the database, including User and Post models.
  - **routes.py:** Defines the routes and view functions for the application.
  - **static/:** Directory for static files such as CSS.
    - **main.css:** CSS styles for the application.
  - **templates/:** Directory for HTML templates used by Flask.
    - **about.html:** Template for the About page.
    - **home.html:** Template for the Home page, displaying posts.
    - **layout.html:** Base template with the site's layout, used by other templates.
    - **login.html:** Template for the Login page.
    - **register.html:** Template for the Registration page.
- **run.py:** Script to run the Flask application.

### Functionality

- **\_\_init\_\_.py:** Initializes the Flask app, sets up the database, and imports routes.
- **forms.py:** Contains the RegistrationForm and LoginForm classes for user input validation.
  - `RegistrationForm`: Fields for username, email, password, and confirmation.
  - `LoginForm`: Fields for email, password, and remember me option.
- **models.py:** Defines SQLAlchemy models for the database.
  - `User`: Model for user accounts with fields for username, email, password, image, and posts.
  - `Post`: Model for recipe posts with fields for title, content, date posted, and author.
- **routes.py:** Defines the routes and view functions for different pages.
  - `/`: Home route displaying all posts.
  - `/about`: About route displaying information about the app.
  - `/register`: Register route for user registration.
  - `/login`: Login route for user login.
- **templates/:** Contains HTML templates rendered by Flask views.
  - **about.html:** About page template.
  - **home.html:** Home page template displaying all posts.
  - **layout.html:** Base template with site layout, used by other templates.
  - **login.html:** Login page template with a form for login.
  - **register.html:** Registration page template with a form for registration.
- **static/:** Directory for static files like CSS.
  - **main.css:** CSS styles for the application's UI.

### How It Works

1. **User Registration and Login:**
   - Users can register for an account with a unique username, email, and password.
   - RegistrationForm in `forms.py` handles user input validation.
   - User data is stored in the `User` model in `models.py`.

2. **Posting Recipes:**
   - Logged-in users can create posts with recipe titles, content, and images.
   - Posts are stored in the `Post` model in `models.py`.
   - Posts are displayed on the Home page (`home.html`) with author names and dates.

3. **Navigation:**
   - The navigation bar in `layout.html` provides links to Home, About, Login, and Register pages.
   - Users can easily navigate between pages using the navigation links.

4. **Styling:**
   - CSS styles in `main.css` define the visual appearance of the application.
   - The layout is designed to be responsive and user-friendly.

### How to Run

1. Make sure you have Python and Flask installed.
2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install required packages:
   ```
   pip install Flask Flask-WTF Flask-SQLAlchemy
   ```
4. Set up the Flask app:
   - Initialize the database:
     ```
     flask db init
     flask db migrate -m "Initial migration"
     flask db upgrade
     ```
   - Run the Flask app:
     ```
     python run.py
     ```
5. Open a web browser and visit `http://localhost:5000/` to view the app.

### Sample Posts

- **How to prepare Jollof Rice:**
  - Author: Ugwu Paschal
  - Description: Learn how to make this flavorful West African dish.
  - Date Posted: April 18, 2024

- **Prepare Egusi Soup Like A Pro:**
  - Author: Amarachi Nnanta
  - Description: A guide to making delicious Nigerian Egusi Soup.
  - Date Posted: April 19, 2024
