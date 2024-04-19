#!/usr/bin/python3
"""Set up a Flask web app.

The app is set to be accessible from any IP address.
Available endpoints:
    /: Displays 'Hello HBNB!' when visited.
    /hbnb: Displays 'HBNB' when visited.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Send the message 'Hello HBNB!' in response to a request."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Send 'HBNB' in response to a request to the '/hbnb' endpoint."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
