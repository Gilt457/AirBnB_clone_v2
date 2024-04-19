#!/usr/bin/python3
"""
Set up a Flask web server.

This server is open to all network interfaces.
It includes these endpoints:
    /: Shows 'Hello HBNB!' when visited.
    /hbnb: Delivers the text 'HBNB' when requested.
    /c/<text>: Shows 'C' plus the text from the URL.
"""
from flask import Flask

# Create an instance of the Flask class.
app = Flask(__name__)


# Define the root route of the web application.
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Serve the welcome message 'Hello HBNB!'."""
    return "Hello HBNB!"


# Define the route for the string 'HBNB'.
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Provide the string 'HBNB' as a response."""
    return "HBNB"


# Define the route for displaying 'C' and the text from the URL.
@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Concatenate 'C' with the text from the URL, replacing"""
    text = text.replace("_", " ")  # Replace underscores.
    return "C {}".format(text)  # Return the formatted string.


# Check if the script is executed as the main program and run the app.
if __name__ == "__main__":
    # Start the Flask web server on all available interfaces.
    app.run(host="0.0.0.0")
