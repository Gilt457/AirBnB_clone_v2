#!/usr/bin/env python3
"""
A Flask web server application with specific routes.

This server will be available on all network interfaces.
Defined routes:
    /: Responds with 'Hello HBNB!' when visited.
    /hbnb: Returns 'HBNB' when accessed.
    /c/<text>: Shows 'C ' followed by the given URL text.
"""
from flask import Flask

# Create an instance of the Flask class
web_app = Flask(__name__)


# Define the route for the root directory
@web_app.route("/", strict_slashes=False)
def greet():
    """Respond with 'Hello HBNB!'."""
    return "Hello HBNB!"


# Define the route for '/hbnb'
@web_app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """Return 'HBNB'."""
    return "HBNB"


# Define the route for '/c/' with a variable path
@web_app.route("/c/<path:text>", strict_slashes=False)
def show_c_text(text):
    """Show 'C ' followed by the text from the URL"""
    return "C " + text.replace("_", " ")


# Run the application if this script is executed as the main program
if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
