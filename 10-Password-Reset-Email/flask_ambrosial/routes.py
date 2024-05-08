#!/usr/bin/env python3
"""Routes and views for the Flask app."""

import secrets
import os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flask_ambrosial import app, db, bcrypt, mail
from flask_ambrosial.forms import (RegistrationForm, LoginForm,
                                   UpdateAccountForm, PostForm,
                                   RequestResetForm, ResetPasswordForm)
from flask_ambrosial.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    image_files = []
    for post in posts:
        image_files.append(url_for('static', filename='post_pics/' + post.image_filename))
    return render_template('home.html', posts=posts, image_files=image_files)


@app.route("/about")
def about():
    """Render the about page."""
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    """Handle user registration.

    If the user is already authenticated, redirects to the home page.
    If the registration form is submitted, validates the form data, hashes
    the password, creates a new user, adds them to the database, and redirects
    to the login page.
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)\
            .decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! \
            You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    """Handle user login.

    If the user is already authenticated, redirects to the home page.
    If the login form is submitted, validates the form data, checks if the
    user exists and the password is correct, logs in the user, and redirects
    to the next page or home page.
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else \
                redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. \
                Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    """Handle user logout.

    Logs out the user and redirects to the home page.
    """
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    """Save and resize the user's profile picture.

    Args:
        form_picture: The file containing the user's profile picture.

    Returns:
        str: The filename of the saved picture.
    """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    """Handle user account settings and update.

    Renders the account page with the update account form. If the form is
    submitted and valid, updates the user's account information and picture.
    """
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        image_file = form.image_filename.data
        if image_file:
            # Save and process the uploaded image if provided
            image_filename = secrets.token_hex(8)
            _, f_ext = os.path.splitext(image_file.filename)
            image_filename = image_filename + f_ext
            image_path = os.path.join(app.root_path, 'static/post_pics', image_filename)
            image_file.save(image_path)
        else:
            # Set image filename to an empty string if no image is uploaded
            image_filename = ''

        # Create a new post with the filename of the uploaded image
        post = Post(title=form.title.data, content=form.content.data, image_filename=image_filename, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        if form.image_filename.data:
            # Save and process the uploaded image if provided
            image_file = form.image_filename.data
            image_filename = secrets.token_hex(8)
            _, f_ext = os.path.splitext(image_file.filename)
            image_filename = image_filename + f_ext
            image_path = os.path.join(app.root_path, 'static/post_pics', image_filename)
            image_file.save(image_path)
            post.image_filename = image_filename
        else:
            post.image_filename = None  # Set image filename to None if no image is uploaded
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('home'))


@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=3)
    image_files = []
    for post in posts:
        image_files.append(url_for('static', filename='post_pics/' + post.image_filename))
    return render_template('user_posts.html', posts=posts, image_files=image_files, user=user)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
