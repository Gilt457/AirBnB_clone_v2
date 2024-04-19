#!/usr/bin/python3
"""
Set up a Flask web server.

This server is set to be accessible from any IP address.
Available endpoints:
    /: Displays 'Hello HBNB!' when visited.
    /hbnb: Displays 'HBNB' when visited.
    /c/<text>: Displays 'C ' followed by the custom <text> provided customer.
    /python/(<text>): Displays 'Python ' followed by the custom <text>.
"""
from flask import Flask

# Create an instance of the Flask class.
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display the welcome message 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display the acronym 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display 'C ' followed by the visitor's input <text>, replacing"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Display 'Python ' followed by the visitor's input <text> replacing"""
    return f"Python {text.replace('_', ' ')}"


# Run the application if this file is executed as the main program.
if __name__ == "__main__":
    # Start the Flask application on all available IPs at port 5000.
    app.run(host="0.0.0.0", port=5000)
