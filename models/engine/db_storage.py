#!/usr/bin/python3
"""Database storage class for SQL Alchemy."""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Create and manage tables using SQLAlchemy."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database connection."""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{passwd}@{host}/{db}',
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return all objects in the database."""
        objects = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = f"{type(elem).__name__}.{elem.id}"
                objects[key] = elem
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for cls in classes:
                query = self.__session.query(cls)
                for elem in query:
                    key = f"{type(elem).__name__}.{elem.id}"
                    objects[key] = elem
        return objects

    def new(self, obj):
        """Add a new object to the database."""
        self.__session.add(obj)

    def save(self):
        """Save changes to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the database."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload database configuration."""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """Close the database session."""
        self.__session.close()
