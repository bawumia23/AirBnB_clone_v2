#!/usr/bin/python3
""" Tests for the Review class. """
import os
import unittest

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Tests for Review. """

    def __init__(self, *args, **kwargs):
        """ Initialize the test. """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "FileStorage default test"
    )
    def test_place_id(self):
        """ Test place_id default type. """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

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
    def test_text(self):
        """ Test text default type. """
        new = self.value()
        self.assertEqual(type(new.text), str)
