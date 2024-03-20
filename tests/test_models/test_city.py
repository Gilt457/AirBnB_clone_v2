#!/usr/bin/python3
"""Unit tests for the City class."""

from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pycodestyle
import unittest
import os


class test_City(test_basemodel):
    """Tests for the City class."""

    def __init__(self, *args, **kwargs):
        """Initialize the City test class."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Ensure state_id is a string."""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Ensure name is a string."""
        new = self.value()
        self.assertEqual(type(new.name), str)


class Test_PEP8(unittest.TestCase):
    """Tests compliance with PEP 8 style guidelines."""

    def test_pep8_user(self):
        """Check that city.py conforms to PEP 8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestCity(unittest.TestCase):
    """Tests for the City class."""

    @classmethod
    def setUpClass(cls):
        """Prepare City class for testing."""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """Clean up after tests."""
        del cls.city

    def tearDown(self):
        """Remove temporary files after each test."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Check that city.py is PEP 8 compliant."""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "Please fix PEP 8 issues.")

    def test_checking_for_docstring_City(self):
        """Verify that the City class has a docstring."""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """Check that City class has the required attributes."""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """Confirm that City is a subclass of BaseModel."""
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def test_attribute_types_City(self):
        """Ensure the attributes of City are of the correct type."""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save_City(self):
        """Test the save method of the City class."""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """Check if converting City instance to a dictionary works."""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
