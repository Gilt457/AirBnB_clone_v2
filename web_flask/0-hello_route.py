#!/usr/bin/python3
"""
This script initializes a Flask web server that serves a simple greeting.
It is configured to listen on all public IPs (0.0.0.0) on port 5000.

Available routes:
    /: Responds with a greeting message 'Hello HBNB!'
"""

# Import the Flask class from the flask module.
from flask import Flask

# Create an instance of the Flask class.
app = Flask(__name__)


# Define the route for the root URL which ignores trailing slashes.
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    A view function that returns the greeting message 'Hello HBNB!'
    when the root URL is accessed.
    """
    return "Hello HBNB!"


# Check if the script is executed directly and not imported.
if __name__ == "__main__":
    # Run the Flask application with the specified host address.
    app.run(host="0.0.0.0")
