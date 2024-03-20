#!/usr/bin/python3
"""City class module."""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place


class City(BaseModel, Base):
    """City class for database representation.

    Attributes:
        state_id (str): State ID to which the city belongs.
        name (str): Official city name.
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship(
        'Place',
        cascade='all, delete, delete-orphan',
        backref='cities'
    )
