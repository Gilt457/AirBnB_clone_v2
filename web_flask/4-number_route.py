#!/usr/bin/python3
"""
Initializes a Flask web server.

This server is configured to listen on all IP addresses (0.0.0.0).
Defined routes:
    /: Returns 'Hello HBNB!' when accessed.
    /hbnb: Returns 'HBNB' when accessed.
    /c/<text>: Returns 'C' plus the text provided in the URL.
    /python/(<text>): Returns 'Python' plus the text provided.
    /number/<n>: Validates if <n> is an integer and returns.
"""
from flask import Flask

# Create an instance of the Flask class.
app = Flask(__name__)


# Define the route for the root URL and return a greeting.
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns a greeting as a string."""
    return "Hello HBNB!"


# Define the route for '/hbnb' URL and return a simple string.
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns a string 'HBNB'."""
    return "HBNB"


# Define the route for '/c/' URL and dynamically.
@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Returns 'C' concatenated with the URL parameter"""
    return f"C {text.replace('_', ' ')}"


# Define the route for '/python/' URL with an optional.
@app.route("/python", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Returns 'Python' concatenated with the URL"""
    return f"Python {text.replace('_', ' ')}"


# Define the route for '/number/' URL and validate.
@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Checks if the parameter is an integer"""
    return f"{n} is a number"


# Check if the script is executed directly and start.
if __name__ == "__main__":
    app.run(host="0.0.0.0")
