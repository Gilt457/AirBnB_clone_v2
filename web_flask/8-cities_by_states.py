#!/usr/bin/python3
"""Initialize a Flask web application.

This app is configured to listen on all public IPs (0.0.0.0) at port 5000.
Defined routes:
    /cities_by_states: Renders an HTML page listing states and their cities.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Render an HTML page listing all states and their corresponding cities.

    The states and cities are ordered alphabetically.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Terminate the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
