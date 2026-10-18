#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone."""

import uuid
from datetime import datetime
from os import getenv

from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all HBNB models."""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(
            DateTime, nullable=False, default=datetime.utcnow
        )
        updated_at = Column(
            DateTime,
            nullable=False,
            default=datetime.utcnow,
            onupdate=datetime.utcnow
        )

    def __init__(self, *args, **kwargs):
        """Initialize a new model instance."""
        if kwargs:
            kwargs = kwargs.copy()
            kwargs['updated_at'] = datetime.fromisoformat(
                kwargs['updated_at']
            )
            kwargs['created_at'] = datetime.fromisoformat(
                kwargs['created_at']
            )
            kwargs.pop('__class__', None)
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            from models import storage
            storage.new(self)

    def __str__(self):
        """Return a string representation of the instance."""
        cls = type(self).__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Update the timestamp and save the instance."""
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        dictionary = self.__dict__.copy()
        dictionary.pop('_sa_instance_state', None)
        dictionary['__class__'] = type(self).__name__

        if isinstance(self.created_at, datetime):
            dictionary['created_at'] = self.created_at.isoformat()
        if isinstance(self.updated_at, datetime):
            dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary

    def delete(self):
        """Delete the current instance from storage."""
        from models import storage

        storage.delete(self)
