#!/usr/bin/python3
"""Base model class for AirBnB clone project."""

from sqlalchemy.ext.declarative import declarative_base
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class BaseModel:
    """Defines common attributes/methods for child classes."""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes the base model with optional kwargs.

        Attributes:
            id (str): A unique UUID.
            created_at (datetime): The creation timestamp.
            updated_at (datetime): The last update timestamp.
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
        """Returns a string representation of the instance."""
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def __repr__(self):
        """Returns an unambiguous string representation of the instance."""
        return self.__str__()

    def save(self):
        """Updates 'updated_at' and saves the instance to storage."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Converts the instance to a dictionary."""
        my_dict = {key: value for key, value in self.__dict__.items()
                   if key != '_sa_instance_state'}
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def delete(self):
        """Deletes the instance from storage."""
        models.storage.delete(self)
