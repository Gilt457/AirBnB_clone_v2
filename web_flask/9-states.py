#!/usr/bin/python3
"""Initialize a Flask web application.

This application is configured to listen on all public IPs.
It defines the following routes:
    /states - returns an HTML page listing all State objects.
    /states/<id> - returns an HTML page for a specific State.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Render an HTML page listing all State objects in alphabetical order."""
    states = storage.all("State").sorted(key=lambda state: state.name)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Render an HTML page for a specific State object"""
    state = storage.all("State").get(id)
    if state:
        return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Close the current SQLAlchemy session after each request."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
