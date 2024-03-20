#!/usr/bin/python3
"""Module for State class definition."""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """State class represents a state within the database.

    Attributes:
        name (str): The name of the state.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Retrieve a list of City objects related to this State instance.

        Returns:
            list: A list of City instances that belong to the State.
        """
        var = models.storage.all()
        city_list = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if city[0] == 'City':
                city_list.append(var[key])
        for city in city_list:
            if city.state_id == self.id:
                result.append(city)
        return result
