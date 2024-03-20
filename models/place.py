#!/usr/bin/python3
"""Place class module"""
from os import getenv
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models

place_amenity = Table(
    "place_amenity", Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"),
           primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey("amenities.id"),
           primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """Place class"""
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
        reviews = relationship(
            "Review", cascade='all, delete, delete-orphan', backref="place"
        )
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False,
            back_populates="place_amenities"
        )
    else:
        @property
        def reviews(self):
            """Get list of reviews.id"""
            all_reviews = models.storage.all()
            review_list = []
            for key in all_reviews:
                if 'Review' in key:
                    review_list.append(all_reviews[key])
            return [
                review for review in review_list if review.place_id == self.id
            ]

        @property
        def amenities(self):
            """Get list of amenity ids"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """Set amenity ids"""
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
