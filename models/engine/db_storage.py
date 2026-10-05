#!/usr/bin/python3
"""This module defines the DBStorage class."""
from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class manages storage of HBNB models in a MySQL database."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database engine."""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user,
                password,
                host,
                database
            ),
            pool_pre_ping=True
        )

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query the current database session for all objects."""
        objects = {}

        classes = [
            State,
            City,
            User,
            Amenity,
            Place,
            Review
        ]

        if cls is not None:
            classes = [cls]

        for model in classes:
            for obj in self.__session.query(model).all():
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objects[key] = obj

        return objects

    def new(self, obj):
        """Add a new object to the current database session."""
        if obj.__class__.__name__ != 'BaseModel':
            self.__session.add(obj)

    def save(self):
        """Commit all changes to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create tables and initialize the database session."""
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )

        self.__session = scoped_session(session_factory)

    def close(self):
        """Remove the current database session."""
        self.__session.remove()
