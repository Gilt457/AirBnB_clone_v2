#!/usr/bin/python3
"""Initialize a Flask web application.

This application is configured to listen on all public.
Defined routes:
    /: Renders the string 'Hello HBNB!' when accessed.
    /hbnb: Renders the string 'HBNB' when accessed.
    /c/<text>: Renders 'C ' followed by the user-provided <text>.
    /python/(<text>): Renders 'Python ' followed by the user-provided.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Render the greeting 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Render the string 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Render 'C ' followed by the user-provided <text>"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Render 'Python ' followed by the user-provided <text>"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
