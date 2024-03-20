#!/usr/bin/python3
"""State class module"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """State class
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """Getter for cities"""
        all_objs = models.storage.all()
        city_list = []
        for key, value in all_objs.items():
            split_key = shlex.split(key.replace('.', ' '))
            if split_key[0] == 'City':
                city_list.append(value)
        return [city for city in city_list if city.state_id == self.id]
