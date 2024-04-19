#!/usr/bin/python3
"""Importing Flask to run the web app"""

# Import necessary modules
from flask import Flask, render_template
from models import storage
from models.state import State

# Create a Flask app instance
app = Flask(__name__)


# Define a function to close the session when the app context is torn down
@app.teardown_appcontext
def close(self):
    """Method to close the session"""
    storage.close()


# Route for displaying a HTML page with states
@app.route('/states', strict_slashes=False)
def state():
    """Displays an HTML page with states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


# Route for displaying an HTML page with cities of a specific state
@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Displays an HTML page with cities of that state"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


# Run the app on host 0.0.0.0 and port 5000
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
