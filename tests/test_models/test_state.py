#!/usr/bin/python3
"""Test module for the State class."""

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class TestState(test_basemodel):
    """TestState class to test the State class."""

    def __init__(self, *args, **kwargs):
        """Initializes TestState."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name_is_string(self):
        """Test if name attribute of State instance is of type str."""
        new_state = self.value()
        self.assertEqual(type(new_state.name), str)
