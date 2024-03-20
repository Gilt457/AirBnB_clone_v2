#!/usr/bin/python3
"""Initialize a Flask web application.

This application is configured to listen on all public IPs.
Defined Routes:
    /states_list: Renders an HTML page listing all State entities.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Render an HTML page that lists State entities from DBStorage.

    The State entities are ordered alphabetically by their name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Terminate the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
