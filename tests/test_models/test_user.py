#!/usr/bin/python3
"""Test User model"""

from tests.test_models.test_base_model import test_basemodel
from models.user import User


class TestUser(test_basemodel):
    """Test cases for User model"""

    def __init__(self, *args, **kwargs):
        """Initialize test instance"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test first name attribute"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test last name attribute"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test email attribute"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test password attribute"""
        new = self.value()
        self.assertEqual(type(new.password), str)
