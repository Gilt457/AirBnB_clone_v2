#!/usr/bin/python3
"""Review class module."""

from sqlalchemy import Column, ForeignKey, String
from models.base_model import Base, BaseModel


class Review(BaseModel, Base):
    """Review entity representation.

    Attributes:
        place_id (str): Place's ID being reviewed.
        user_id (str): ID of the user writing the review.
        text (str): Review content.
    """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
