#!/usr/bin/python3
"""Initializes a Flask web server.

This server is configured to listen on all IP addresses (0.0.0.0).
Defined routes:
    /: Returns 'Hello HBNB!' when accessed.
    /hbnb: Returns 'HBNB' when this route is visited.
    /c/<text>: Returns 'C' plus the text provided in the URL.
    /python/(<text>): Returns 'Python' plus the text provided
    /number/<n>: Returns '<n> is a number' if <n> is an integer.
    /number_template/<n>: Serves an HTML page if <n> is an integer.
"""

# Flask library imported to create the application
from flask import Flask, render_template

# Flask application instance created
app = Flask(__name__)


# Route to respond with 'Hello HBNB!'
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Responds with 'Hello HBNB!'"""
    return "Hello HBNB!"


# Route to respond with 'HBNB'
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Responds with 'HBNB'"""
    return "HBNB"


# Route to display 'C' and the subsequent text
@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Responds with 'C' and the text from the URL"""
    return f"C {text.replace('_', ' ')}"


# Route to display 'Python' and the subsequent text
@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Responds with 'Python' and the text from the URL'"""
    return f"Python {text.replace('_', ' ')}"


# Route to confirm if the provided value is a number
@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Confirms that the provided value is a number"""
    return f"{n} is a number"


# Route to display an HTML page if the provided value is a number
@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Serves an HTML page if the value is a number"""
    return render_template("5-number.html", n=n)


# Main execution point to run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0")
