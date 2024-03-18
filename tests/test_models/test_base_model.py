#!/usr/bin/python3
"""Unit tests for BaseModel class"""

import unittest
import datetime
import json
import os
import inspect
import pycodestyle
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up test environment"""
        self.base = BaseModel()
        self.base.name = "Kev"
        self.base.num = 20

    def tearDown(self):
        """Tear down test environment"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Test for PEP 8 compliance"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP 8 issues")

    def test_checking_for_docstring_BaseModel(self):
        """Check for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """Check if BaseModel has methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """Test if the base is an instance of BaseModel"""
        self.assertIsInstance(self.base, BaseModel)

    def test_save_BaseModel(self):
        """Test if save method works"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """Test if to_dict method works"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


class TestCodeFormat(unittest.TestCase):
    """Test cases for code formatting"""

    def test_pycodestyle(self):
        """Test PEP 8 compliance"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDocstrings(unittest.TestCase):
    """Test cases for docstrings"""

    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        cls.obj_members(BaseModel, inspect.isfunction)

    def test_docstrings(self):
        """Test presence of docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)


if __name__ == "__main__":
    unittest.main()
