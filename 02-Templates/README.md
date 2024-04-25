# Flask Ambrosial Web Application

This project consists of a Flask web application that showcases a our Ambrosial website. Below, we'll break down each component and its significance in building the application.

.
├── README.md
├── flask.ambrosial.py
├── static
│   └── main.css
└── templates
    ├── about.html
    ├── home.html
    └── layout.html

2 directories, 6 files

## flask_ambrosial.py
- **Flask Initialization:** This file hosts our Flask application.
- **Imports:** We import the Flask class and necessary functions (`render_template`, `url_for`) from the Flask package.
- **App Setup:** We create an instance of the Flask class and assign it to the variable `app`.
- **Data Representation:** A list called `posts` holds dictionaries representing blog posts.
- **Routing:** Two routes (`/` and `/home`) are defined using the `@app.route` decorator to handle requests.
- **View Functions:** Functions like `home()` and `about()` are associated with routes, rendering HTML templates via `render_template`.

## about.html
- **Template Inheritance:** Extends a base layout template (`layout.html`) using `{% extends "layout.html" %}`.
- **Content Definition:** Inside `{% block content %} ... {% endblock %}` tags, it defines the About page content, which is a simple `<h1>` heading.

## home.html
- **Dynamic Content:** Extends `layout.html` and defines Home page content.
- **Iteration:** Uses a `for` loop inside `{% block content %} ... {% endblock %}` to iterate over `posts` for dynamic HTML generation, displaying author, date, title, and content.

## layout.html
- **Base Layout:** Serves as the foundation for our web pages.
- **Structure:** Defines the layout, including header, navigation, main content area, and sidebar, ensuring consistency.
- **Bootstrap Integration:** Includes Bootstrap CSS and JavaScript for styling and interactivity.
- **Jinja Templating:** Uses Jinja2 to conditionally render the page title and include a separate CSS file (`main.css`).
- **Content Blocks:** `{% block content %} ... {% endblock %}` tags specify where content for each page will be inserted.

## main.css
- **Styling:** Contains styles for colors, fonts, layout, and spacing.
- **Consistency:** Ensures uniform appearance across all pages.
- **Customization:** Allows modification of various elements to match design preferences.

This project amalgamates these components to form a simple Flask web application presenting a list of posts on the Home page and a basic About page. The layout and styling are facilitated by Bootstrap and custom CSS, while Flask handles routing and template rendering.
