#!/usr/bin/python3
"""Set up a Flask web server.

This server is set to be accessible on all interfaces.
Available endpoints:
    /: Displays 'Hello HBNB!' when visited.
    /hbnb: Displays 'HBNB' when visited.
    /c/<custom_text>: Displays 'C ' followed by the provided <custom_text>.
    /python/(<custom_text>): Displays 'Python ' followed by the provided
"""
from flask import Flask

web_app = Flask(__name__)  # Create a Flask application instance


@web_app.route("/", strict_slashes=False)
def greet_hbnb():
    """Display the welcome message 'Hello HBNB!'."""
    return "Hello HBNB!"


@web_app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """Display the string 'HBNB'."""
    return "HBNB"


@web_app.route("/c/<custom_text>", strict_slashes=False)
def show_c_with_text(custom_text):
    """Display 'C ' followed by the provided <custom_text>"""
    custom_text = custom_text.replace("_", " ")
    return "C {}".format(custom_text)


@web_app.route("/python", strict_slashes=False)
@web_app.route("/python/<custom_text>", strict_slashes=False)
def show_python_with_text(custom_text="is awesome"):
    """Display 'Python ' followed by the provided <custom_text>"""
    custom_text = custom_text.replace("_", " ")
    return "Python {}".format(custom_text)


if __name__ == "__main__":
    web_app.run(host="0.0.0.0")  # Start the application
