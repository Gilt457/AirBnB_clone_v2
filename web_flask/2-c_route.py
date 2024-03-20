#!/usr/bin/python3
"""Initialize a Flask web application.

This application is configured to listen on all public.
It defines the following routes:
    /: Renders a greeting 'Hello HBNB!' when accessed.
    /hbnb: Returns the string 'HBNB' upon access.
    /c/<text>: Displays 'C' followed by the text passed in the URL.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Render the greeting 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return the string 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display 'C' followed by the URL-passed text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
