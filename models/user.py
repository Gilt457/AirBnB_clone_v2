#!/usr/bin/python3
"""User class module."""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place as Plc
from models.review import Review as Rev


class User(BaseModel, Base):
    """User entity representation.

    Attributes:
        email (str): User's email.
        password (str): User's password.
        first_name (str): User's first name.
        last_name (str): User's last name.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Plc", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Rev", cascade='all, delete, delete-orphan',
                           backref="user")
