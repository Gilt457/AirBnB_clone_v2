#!/usr/bin/python3
"""Base model class for AirBnB"""
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import models
import uuid

Base = declarative_base()


class BaseModel:
    """Defines common attributes/methods for other classes"""
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Base model class instantiation
        Args:
            args: not used
            kwargs: arguments for BaseModel constructor
        Attributes:
            id: unique id
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            self.id = kwargs.get("id", str(uuid.uuid4()))
            self.created_at = kwargs.get("created_at", datetime.now())
            self.updated_at = kwargs.get("updated_at", datetime.now())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string of class name, id, and dictionary"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def __repr__(self):
        """Returns a string representation"""
        return self.__str__()

    def save(self):
        """Updates the public instance attribute updated_at to current"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Creates dictionary of the class and returns"""
        my_dict = {**self.__dict__}
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop('_sa_instance_state', None)
        return my_dict

    def delete(self):
        """Deletes object"""
        models.storage.delete(self)
