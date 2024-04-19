#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def display_c(text):
    # Replace underscores with spaces
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"


@app.route('/python/<text>')
def display_python(text="is cool"):
    # Replace underscores with spaces
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, strict_slashes=False)
