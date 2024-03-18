#!/usr/bin/python3
"""Unit tests for Review class."""

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class TestReview(test_basemodel):
    """Test Review class."""

    def __init__(self, *args, **kwargs):
        """Initialize TestReview."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.model = Review

    def test_place_id(self):
        """Test place_id attribute."""
        new_review = self.model()
        self.assertEqual(type(new_review.place_id), str)

    def test_user_id(self):
        """Test user_id attribute."""
        new_review = self.model()
        self.assertEqual(type(new_review.user_id), str)

    def test_text(self):
        """Test text attribute."""
        new_review = self.model()
        self.assertEqual(type(new_review.text), str)
