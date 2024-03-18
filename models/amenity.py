#!/usr/bin/python3
"""
This module defines the Amenity class.
"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """
    A class representing amenities.

    Attributes:
        name (str): The name of the amenity.
    """

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
