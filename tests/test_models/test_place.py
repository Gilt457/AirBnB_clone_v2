#!/usr/bin/python3
"""Test suite for the Place class."""

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Test cases for the Place class."""

    def __init__(self, *args, **kwargs):
        """Initialize the test case with Place class setup."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Ensure the city_id attribute is a string."""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Ensure the user_id attribute is a string."""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Ensure the name attribute is a string."""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Ensure the description attribute is a string."""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Ensure the number_rooms attribute is an integer."""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Ensure the number_bathrooms attribute is an integer."""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Ensure the max_guest attribute is an integer."""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Ensure the price_by_night attribute is an integer."""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Ensure the latitude attribute is a float."""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Ensure the longitude attribute is a float."""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """Ensure the amenity_ids attribute is a list."""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
