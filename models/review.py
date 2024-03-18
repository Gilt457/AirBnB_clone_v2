#!/usr/bin/python3
"""
This module defines the Review class.
"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Review(BaseModel, Base):
    """
    Review class to represent reviews.
    Attributes:
        place_id (str): Place ID.
        user_id (str): User ID.
        text (str): Review description.
    """
    __tablename__ = "reviews"

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
