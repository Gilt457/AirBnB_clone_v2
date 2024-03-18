#!/usr/bin/python3
"""Create a unique FileStorage instance for the application."""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv


def get_storage_instance():
    """Return an appropriate storage instance based on HBNB_TYPE_STORAGE."""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        return DBStorage()
    else:
        return FileStorage()


storage = get_storage_instance()
storage.reload()