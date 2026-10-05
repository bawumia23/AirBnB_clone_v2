#!/usr/bin/python3
""" Tests for the User class. """
import os
import unittest

from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Tests for User. """

    def __init__(self, *args, **kwargs):
        """ Initialize the test. """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_first_name(self):
        """ Test first_name default type. """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_last_name(self):
        """ Test last_name default type. """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_email(self):
        """ Test email default type. """
        new = self.value()
        self.assertEqual(type(new.email), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_password(self):
        """ Test password default type. """
        new = self.value()
        self.assertEqual(type(new.password), str)
