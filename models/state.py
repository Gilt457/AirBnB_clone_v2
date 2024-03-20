#!/usr/bin/python3
"""Module for State class definition."""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """Representation of 'State' which maps to 'states' table in the database.

    Attributes:
        name (str): The name of the state.
        cities (relationship): The relationship to the 'City' class.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete, delete-orphan',
                          backref='state')

    @property
    def cities(self):
        """Property that returns cities related to the state."""
        all_cities = models.storage.all()
        city_list = []
        related_cities = []
        for key, value in all_cities.items():
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if city[0] == 'City':
                city_list.append(value)
        for city in city_list:
            if city.state_id == self.id:
                related_cities.append(city)
        return related_cities
