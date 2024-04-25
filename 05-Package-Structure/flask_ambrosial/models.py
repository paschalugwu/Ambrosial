#!/usr/bin/env python3

# Import necessary modules
from flask_ambrosial import db
from datetime import datetime, timezone


# Define User model for database
class User(db.Model):
    """
    Model for user data stored in the database.

    Attributes:
        id (int): Unique identifier for the user.
        username (str): Username of the user (max length: 20 characters).
        email (str): Email address of the user (max length: 120 characters).
        image_file (str): File path to the user's profile image.
        password (str): Hashed password of the user.
        posts (relationship): Relationship with Post model, \
            representing user's posts.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        """
        Method to represent the User object as a string.

        Returns:
            str: String representation of the User object.
        """
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


# Define Post model for database
class Post(db.Model):
    """
    Model for post data stored in the database.

    Attributes:
        id (int): Unique identifier for the post.
        title (str): Title of the post (max length: 100 characters).
        date_posted (datetime): Date and time when the post was created.
        content (str): Content of the post.
        user_id (int): Foreign key referencing the user who created the post.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now(timezone.utc))
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """
        Method to represent the Post object as a string.

        Returns:
            str: String representation of the Post object.
        """
        return f"Post('{self.title}', '{self.date_posted}')"
