### Ambrosial - User Account & Profile Picture Management App

```
flask_ambrosial/
│
├── flask_ambrosial/
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   │   └── main.css
│   └── templates/
│       ├── account.html
│       ├── home.html
│       ├── layout.html
│       ├── login.html
│       └── register.html
│
├── venv/
│
├── run.py
│
└── README.md
```

---

#### Introduction

Ambrosial is a Flask application designed to manage user accounts and facilitate profile picture uploads. It offers a seamless experience for users to register, log in, update their account information, and upload profile pictures. This README provides an in-depth overview of the application's structure, functionalities, and usage instructions.

---

#### Application Structure

The Ambrosial application is structured as follows:

- **flask_ambrosial/**: The core directory containing application files and subdirectories.
  - **\_\_init\_\_.py**: Initializes the Flask application.
  - **forms.py**: Defines forms for user registration, login, and account update.
  - **models.py**: Defines database models for user accounts.
  - **routes.py**: Defines application routes and functionalities.
  - **static/**: Stores static files like CSS.
  - **templates/**: Contains HTML templates for rendering web pages.
    - **account.html**: Displays user account information and allows for updates.
    - **home.html**: Renders the home page with posts.
    - **layout.html**: Base template providing the overall structure of web pages.
    - **login.html**: Renders the login page.
    - **register.html**: Renders the registration page.
- **venv/**: Virtual environment directory.
- **run.py**: Entry point for running the Flask application.

---

#### Application Functionality

Ambrosial offers the following features:

1. **Registration**: Users can sign up for an account by providing a username, email, and password. Passwords are securely hashed before storage.

2. **Login**: Registered users can log in using their email and password credentials.

3. **Account Management**: Logged-in users have the ability to update their username and email.

4. **Profile Picture Upload**: Users can upload a profile picture during account registration or update.

---

#### How to Run

To run the Ambrosial application, follow these steps:

1. **Setup Environment**:
   - Ensure Python and pip are installed on your system.

2. **Create Virtual Environment**:
   - Run `python3 -m venv venv` to create a virtual environment.

3. **Activate Virtual Environment**:
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`

4. **Install Dependencies**:
   - Run `pip install -r requirements.txt` to install required packages.

5. **Run the Application**:
   - Execute `python run.py` to start the Flask application.

6. **Access the Application**:
   - Open your web browser and navigate to `http://localhost:5000` to access Ambrosial.

---

#### Conclusion

Ambrosial provides a robust solution for user account management and profile picture uploads within a Flask environment. Its structured architecture, intuitive functionalities, and clear usage instructions make it an ideal choice for developers looking to implement similar features in their web applications.

---
