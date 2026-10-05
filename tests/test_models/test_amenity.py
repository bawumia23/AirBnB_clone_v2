#!/usr/bin/python3
""" Tests for the Amenity class. """
import os
import unittest

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Tests for Amenity. """

    def __init__(self, *args, **kwargs):
        """ Initialize the test. """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_name2(self):
        """ Test name default type. """
        new = self.value()
        self.assertEqual(type(new.name), str)
