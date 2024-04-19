#!/usr/bin/python3
"""Initialize a Flask web application.

This app is configured to listen on all public IPs (0.0.0.0) at port 5000.
Defined routes:
    /cities_by_states: Renders an HTML page listing states and their cities.
"""
from models import storage
from flask import Flask, render_template

# Create an instance of the Flask class.
app = Flask(__name__)


# Define the route for 'cities_by_states'.
@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Render an HTML page listing all states and their corresponding cities.

    States and cities are retrieved from storage and sorted alphabetically.
    """
    # Retrieve all 'State' objects from storage.
    states = storage.all("State").values()
    # Sort states by name.
    sorted_states = sorted(states, key=lambda state: state.name)
    # Render the HTML template with sorted states.
    return render_template("8-cities_by_states.html", states=sorted_states)


# Define the teardown function for the application context.
@app.teardown_appcontext
def teardown_db_session(exc):
    """Close the SQLAlchemy session after each request."""
    storage.close()


# Run the application if this file is executed as the main program.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
