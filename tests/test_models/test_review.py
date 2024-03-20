#!/usr/bin/python3
"""Test suite for the Review class."""

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Test cases for the Review class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize the test case with Review class specifics
        and inherit from test_basemodel.
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """
        Test if the place_id attribute of a new Review instance
        is a string type.
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """
        Test if the user_id attribute of a new Review instance
        is a string type.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """
        Test if the text attribute of a new Review instance
        is a string type.
        """
        new = self.value()
        self.assertEqual(type(new.text), str)
