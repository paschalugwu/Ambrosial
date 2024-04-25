#!/usr/bin/env python3

# Import the Flask application instance from flask_ambrosial package
from flask_ambrosial import app

# Check if the script is being run directly by the Python interpreter
if __name__ == '__main__':
    """ Run the Flask application
     - debug=True enables debug mode, allowing for live code \
         reloading and better error messages
     - This is the entry point of the application, where Flask \
         starts listening for requests
    """
    app.run(debug=True)
