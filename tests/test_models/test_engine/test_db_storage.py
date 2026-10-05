#!/usr/bin/python3
"""Module for testing DBStorage."""
import unittest
from os import getenv

from models import storage
from models.state import State
from models.engine.db_storage import DBStorage


@unittest.skipUnless(
    getenv('HBNB_TYPE_STORAGE') == 'db',
    "Tests only for DBStorage"
)
class TestDBStorage(unittest.TestCase):
    """Tests for the DBStorage class."""

    def setUp(self):
        """Set up the test environment."""
        self.storage = storage
        self.storage.reload()

    def tearDown(self):
        """Clean up the database session."""
        self.storage.close()

    def test_storage_type(self):
        """Test that storage is an instance of DBStorage."""
        self.assertIsInstance(self.storage, DBStorage)

    def test_all_empty(self):
        """Test all() with an empty database."""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        """Test adding an object to the database session."""
        obj = State()
        obj.name = 'California'

        key = 'State.{}'.format(obj.id)

        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test saving an object to the database."""
        obj = State()
        obj.name = 'California'

        key = 'State.{}'.format(obj.id)

        self.storage.save()

        self.assertIn(key, self.storage.all())

    def test_delete(self):
        """Test deleting an object from the database."""
        obj = State()
        obj.name = 'California'

        key = 'State.{}'.format(obj.id)

        self.storage.save()
        self.assertIn(key, self.storage.all())

        self.storage.delete(obj)
        self.storage.save()

        self.assertNotIn(key, self.storage.all())

    def test_reload(self):
        """Test that reload creates a usable session."""
        self.storage.reload()
        self.assertIsNotNone(self.storage._DBStorage__session)

    def test_close(self):
        """Test that close removes the current session."""
        self.storage.reload()
        self.storage.close()
        self.assertIsNotNone(self.storage._DBStorage__session)


if __name__ == '__main__':
    unittest.main()
