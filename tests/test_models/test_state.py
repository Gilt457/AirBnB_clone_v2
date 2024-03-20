#!/usr/bin/python3
"""Module to test the State class functionality."""

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Test suite for the State class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize the test_state instance and inherit.
        Set the name attribute to 'State' and the value.
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """
        Test the type of the 'name' attribute in a new State instance.
        Assert that it is of type 'str'.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
