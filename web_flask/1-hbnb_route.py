#!/usr/bin/python3
"""
Flask web application with custom routes.

Routes:
    /: Returns the message 'Welcome to My Web App!' when accessed.
    /about: Returns the string 'About Us' when accessed.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def welcome():
    """Return the message 'Welcome to My Web App!"""
    return "Welcome to My Web App!"


@app.route("/about", strict_slashes=False)
def about():
    """Return 'About Us' when the '/about' route is requested."""
    return "About Us"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
