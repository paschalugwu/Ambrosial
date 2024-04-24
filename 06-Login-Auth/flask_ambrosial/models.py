#!/usr/bin/env python3
"""Database models for User and Post entities."""

from flask_ambrosial import db, login_manager
from datetime import datetime, timezone
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    """Load a user by ID for Flask-Login."""
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """User model for storing user information."""
    
    # User attributes: id, username, email, image_file, password
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    
    # Relationship with Post model, one-to-many relationship (one user can have multiple posts)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        """Representation of the User object."""
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    """Post model for storing user posts."""
    
    # Post attributes: id, title, date_posted, content, user_id
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    content = db.Column(db.Text, nullable=False)
    
    # Foreign key relationship with User model, each post belongs to a user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        """Representation of the Post object."""
        return f"Post('{self.title}', '{self.date_posted}')"
