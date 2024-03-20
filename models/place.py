#!/usr/bin/python3
"""Class definition for Place"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models

# Define a table to link Place and Amenity classes
place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """Place class
    Attributes:
        city_id: ID of the city
        user_id: ID of the user
        name: Name of the place
        description: Description of the place
        number_rooms: Number of rooms as an integer
        number_bathrooms: Number of bathrooms as an integer
        max_guest: Maximum number of guests as an integer
        price_by_night: Price per night as an integer
        latitude: Latitude as a float
        longitude: Longitude as a float
        amenity_ids: List of Amenity IDs
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        # Define a relationship between Place and Review
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        # Define a relationship between Place and Amenity
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """Return a list of review IDs"""
            var = models.storage.all()
            lista = []
            result = []
            for key in var:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    lista.append(var[key])
            for elem in lista:
                if (elem.place_id == self.id):
                    result.append(elem)
            return (result)

        @property
        def amenities(self):
            """Return a list of amenity IDs"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """Add an amenity ID to the list"""
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
