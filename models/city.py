#!/usr/bin/python3
"""This module defines the City class."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.place import Place


class City(BaseModel, Base):
    """City class for representing cities."""

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
