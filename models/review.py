#!/usr/bin/python3
"""
This is a class for handling reviews.
"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Review(BaseModel, Base):
    """
    This class represents a Review.
    Attributes:
        place_id: The ID of the place.
        user_id: The ID of the user.
        text: The description of the review.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
