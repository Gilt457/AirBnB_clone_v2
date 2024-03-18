#!/usr/bin/python3
"""Module to test City class."""

import unittest
import os
import pycodestyle
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City class."""

    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """Clean up after test."""
        del cls.city

    def tearDown(self):
        """Tear down test."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8(self):
        """Test PEP 8 compliance."""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP8")

    def test_docstring(self):
        """Test for presence of docstring."""
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """Test for presence of attributes."""
        attributes = ['id', 'created_at', 'updated_at', 'state_id', 'name']
        for attr in attributes:
            self.assertTrue(hasattr(self.city, attr))

    def test_is_subclass(self):
        """Test if City is a subclass of BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attribute_types(self):
        """Test attribute types."""
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)

    def test_save(self):
        """Test if save works."""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """Test to_dict method."""
        self.assertTrue('to_dict' in dir(self.city))


class TestPEP8(unittest.TestCase):
    """Test PEP 8 compliance."""

    def test_pep8(self):
        """Test for PEP 8 compliance."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
