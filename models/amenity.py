#!/usr/bin/python3
""" Amenity Module for HBNB project """
from os import getenv

from sqlalchemy import Column, String

from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = 'amenities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
