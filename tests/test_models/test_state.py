#!/usr/bin/python3
""" Tests for the State class. """
import os
import unittest

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Tests for State. """

    def __init__(self, *args, **kwargs):
        """ Initialize the test. """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_name3(self):
        """ Test name default type. """
        new = self.value()
        self.assertEqual(type(new.name), str)
