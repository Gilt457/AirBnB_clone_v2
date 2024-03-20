#!/usr/bin/python3
"""Module containing the Amenity class which inherits"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Representation of an Amenity entity.

    This class is used to represent amenities available in places.

    Attributes:
        name (str): The name of the amenity.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
