#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv

from sqlalchemy import (
    Column, Float, ForeignKey, Integer, String, Table
)
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False
    )
)


class _AmenityList(list):
    """List that records amenity IDs on its associated place."""

    def __init__(self, place, amenities):
        super().__init__(amenities)
        self._place = place

    def append(self, obj):
        """Append an Amenity and record its ID if it is valid."""
        from models.amenity import Amenity

        if isinstance(obj, Amenity):
            if obj.id not in self._place.amenity_ids:
                self._place.amenity_ids.append(obj.id)
            super().append(obj)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(
            String(60),
            ForeignKey('cities.id'),
            nullable=False
        )
        user_id = Column(
            String(60),
            ForeignKey('users.id'),
            nullable=False
        )
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        user = relationship(
            'User',
            back_populates='places'
        )
        reviews = relationship(
            'Review',
            back_populates='place',
            cascade='all, delete-orphan'
        )
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False,
            back_populates='place_amenities'
        )
        cities = relationship(
            'City',
            back_populates='places'
        )
        amenity_ids = []
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """Return reviews associated with this place."""
            from models import storage
            from models.review import Review

            return [
                review for review in storage.all(Review).values()
                if review.place_id == self.id
            ]

        @property
        def amenities(self):
            """Return amenities associated with this place."""
            from models import storage
            from models.amenity import Amenity

            all_amenities = storage.all(Amenity).values()
            matching = [
                amenity for amenity in all_amenities
                if amenity.id in self.amenity_ids
            ]
            return _AmenityList(self, matching)

        @amenities.setter
        def amenities(self, obj):
            """Add an amenity ID when an Amenity object is assigned."""
            from models.amenity import Amenity

            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
