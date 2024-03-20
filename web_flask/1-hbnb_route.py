#!/usr/bin/python3
"""Initialize a Flask web application.

This application is configured to listen on all public IPs (0.0.0.0).
Defined routes:
    /: Returns the string 'Hello HBNB!' when accessed.
    /hbnb: Returns the string 'HBNB' when accessed.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Return the greeting 'Hello HBNB!' when the root route is requested."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return 'HBNB' when the '/hbnb' route is requested."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
