#!/usr/bin/python3
"""This script initializes a unique instance of FileStorage"""

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

# Determine the type of storage to use based on environment variable
if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()  # Use database storage if specified
else:
    storage = FileStorage()  # Fallback to file storage

storage.reload()  # Load existing data from storage
