#!/usr/bin/python3
"""Initializes a Flask web server.

This server is configured to listen on all interfaces, port 5000.
Defined routes:
    /: Returns 'Hello HBNB!' when accessed.
    /hbnb: Returns 'HBNB' when accessed.
    /c/<text>: Returns 'C' plus the text provided in the URL.
    /python/(<text>): Returns 'Python' plus the text provided,
    with a default text if none is given.
    /number/<n>: Confirms that 'n' is a number if 'n' is an integer.
    /number_template/<n>: Serves a web page if 'n' is an integer,
     displaying 'n' within the page.
    /number_odd_or_even/<n>: Serves a web page if 'n' is an integer,
    indicating if 'n' is odd or even.
"""
from flask import Flask, render_template

app = Flask(__name__)
# Configure Jinja to remove excess whitespace around blocks
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns a greeting message featuring 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns the string 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Returns 'C' and the user-provided URL text,

    with any underscores turned into spaces"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Returns 'Python' and the user-provided URL text,

    with any underscores turned into spaces, and a default"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Confirms that the provided 'n' is a number if it's an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Serves a web page that displays the integer 'n'

    within the page body if 'n' is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Serves a web page that indicates whether the integer 'n'

    is odd or even within the page body"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
