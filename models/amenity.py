#!/usr/bin/python3
"""
This module contains the class Amenity which inherits from BaseModel and Base.
"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """
    This class represents an Amenity entity and is used to represent amenities
    available in places.

    Attributes:
        name (str): The name of the amenity.
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary=place_amenity)
