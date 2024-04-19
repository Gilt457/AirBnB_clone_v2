#!/usr/bin/python3
"""Set up a Flask web server.

This server is open to all network interfaces (0.0.0.0) and uses port 5000.
It includes the following endpoint:
    /cities_by_states: Displays a web page with a list of states.
"""
from models import storage  # Import the storage module from models package.
from flask import Flask, render_template

app = Flask(__name__)  # Create an instance of the Flask class.


# Define a route for the URL '/cities_by_states'.
@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Serve a web page that shows a list of states along with their cities.

    Retrieves and sorts the states and their cities in alphabetical order.
    """
    states = storage.all("State")  # Get all 'State' objects from the storage.
    # Render the HTML template with the list of states.
    return render_template("8-cities_by_states.html", states=states)


# Define a function to be called when the app context is torn down.
@app.teardown_appcontext
def teardown(exc):
    """Close the current SQLAlchemy session after the request ends."""
    storage.close()  # Close the storage connection.


# Check if the script is executed as the main program.
if __name__ == "__main__":
    # Run the Flask app with the specified host address.
    app.run(host="0.0.0.0")
