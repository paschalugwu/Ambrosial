**Ambrosial: A Flask-Based Social Media Platform**

**README**

---

### Overview

Ambrosial is a social media platform built using Flask, a Python web framework. It provides users with features such as user registration, login, posting, profile management, and password reset functionality. This README provides a detailed overview of the project structure, functionality, and interactions between various components of the application.

### Project Structure

The project structure follows a typical Flask application layout:

- **flask_ambrosial**: This directory contains the main application code.
  - **\_\_init\_\_.py**: Initializes the Flask application and its extensions.
  - **forms.py**: Defines Flask-WTF forms for user registration, login, account update, post creation, password reset request, and password reset.
  - **models.py**: Defines SQLAlchemy database models for User and Post entities.
  - **routes.py**: Defines the routes and views for the application.
  - **templates/**: Contains HTML templates for rendering pages.
  - **static/**: Contains static files such as CSS, JavaScript, and images.
- **tests/**: Contains unit tests for testing various components of the application.
- **venv/**: Virtual environment directory for managing dependencies.

### Functionality

1. **User Registration and Login**:
   - Users can register by providing a username, email, and password.
   - Passwords are hashed using Bcrypt for security.
   - Registered users can log in using their email and password.

2. **User Account Management**:
   - Registered users can update their username, email, and profile picture.
   - Profile pictures are resized and saved in the 'static/profile_pics' directory.

3. **Posting**:
   - Logged-in users can create new posts with a title, content, and optional image upload.
   - Posts are associated with the user who created them.
   - Images uploaded with posts are saved in the 'static/post_pics' directory.

4. **Password Reset**:
   - Users who forget their passwords can request a password reset.
   - An email with a password reset link is sent to the user's registered email address.
   - The reset link contains a unique token generated using itsdangerous for security.
   - Users can reset their password by providing a new password and confirming it.

### Interactions and Behaviors

1. **User Registration and Login**:
   - When a user registers, their information is validated, and if successful, a new user record is created in the database.
   - During login, the user's credentials are validated, and if correct, they are logged in and redirected to the home page.
   - If login fails, an error message is displayed.

2. **User Account Management**:
   - When a user updates their account information, the changes are validated and saved to the database.
   - If the user uploads a new profile picture, it is resized and saved in the 'static/profile_pics' directory.

3. **Posting**:
   - When a user creates a new post, the post data is validated, and if successful, a new post record is created in the database.
   - If an image is uploaded with the post, it is resized and saved in the 'static/post_pics' directory.

4. **Password Reset**:
   - When a user requests a password reset, an email with a reset link is sent to their registered email address.
   - The reset link contains a token that expires after a certain time (30 minutes by default).
   - If the user resets their password within the allowed time frame, their password is updated, and they can log in with the new password.

### Conclusion

Ambrosial is a feature-rich social media platform built using Flask and various extensions. It provides users with a seamless experience for registration, login, posting, profile management, and password reset. The application's codebase is well-structured, and interactions between components are efficiently handled to ensure smooth functionality. With its intuitive user interface and robust features, Ambrosial offers a compelling platform for social networking and content sharing.
