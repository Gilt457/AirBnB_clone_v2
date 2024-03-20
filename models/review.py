#!/usr/bin/python3
"""Module for Review class."""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Representation of a Review entity.

    Attributes:
        place_id (str): Identifier of the place being reviewed.
        user_id (str): Identifier of the user who wrote the review.
        text (str): Content of the review.
    """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
