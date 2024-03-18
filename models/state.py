#!/usr/bin/python3
"""This is the state class"""

import shlex
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities_rel = relationship("City", cascade='all, delete, delete-orphan',
                              backref="state")

    @property
    def cities(self):
        all_models = models.storage.all()
        cities_list = []
        result = []
        for key in all_models:
            city_name = key.replace('.', ' ')
            city_name = shlex.split(city_name)
            if city_name[0] == 'City':
                cities_list.append(all_models[key])
        for elem in cities_list:
            if elem.state_id == self.id:
                result.append(elem)
        return result
