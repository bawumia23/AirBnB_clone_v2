#!/usr/bin/python3
"""PlaceAmenity model for the HBNB project."""
from os import getenv

from models.base_model import Base
from models.place import place_amenity


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class PlaceAmenity(Base):
        """Association between a Place and an Amenity."""
        __table__ = place_amenity
else:
    class PlaceAmenity:
        """Association between a Place and an Amenity."""
        pass
