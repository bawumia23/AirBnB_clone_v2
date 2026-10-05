#!/usr/bin/python3
""" Tests for the Place class. """
import os
import unittest

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Tests for Place. """

    def __init__(self, *args, **kwargs):
        """ Initialize the test. """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_city_id(self):
        """ Test city_id default type. """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_user_id(self):
        """ Test user_id default type. """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_name(self):
        """ Test name default type. """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_description(self):
        """ Test description default type. """
        new = self.value()
        self.assertEqual(type(new.description), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_number_rooms(self):
        """ Test number_rooms default type. """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_number_bathrooms(self):
        """ Test number_bathrooms default type. """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_max_guest(self):
        """ Test max_guest default type. """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_price_by_night(self):
        """ Test price_by_night default type. """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_latitude(self):
        """ Test latitude default type. """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_longitude(self):
        """ Test longitude default type. """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Test amenity_ids default type. """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
