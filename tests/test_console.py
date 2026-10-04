#!/usr/bin/python3
"""Unit tests for the HBNB console's parameterized create command."""
import os
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') == 'db',
    "parameterized create is only tested with FileStorage"
)
class TestCreateWithParams(unittest.TestCase):
    """Tests for 'create <Class> <key>=<value> ...'."""

    def setUp(self):
        """Start every test from empty storage and no file.json."""
        storage.all().clear()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Remove file.json created during the test."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def _create(self, command):
        """Run a console command and return its stripped output."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(command)
        return output.getvalue().strip()

    def test_string_param(self):
        """A quoted value becomes a string attribute."""
        new_id = self._create('create State name="California"')
        obj = storage.all()["State." + new_id]
        self.assertEqual(obj.name, "California")

    def test_underscores_to_spaces(self):
        """Underscores inside quoted strings are converted to spaces."""
        new_id = self._create('create Place name="My_little_house"')
        obj = storage.all()["Place." + new_id]
        self.assertEqual(obj.name, "My little house")

    def test_integer_param(self):
        """Numeric values without decimals are converted to int."""
        new_id = self._create('create Place number_rooms=4')
        obj = storage.all()["Place." + new_id]
        self.assertEqual(obj.number_rooms, 4)
        self.assertIsInstance(obj.number_rooms, int)

    def test_float_param(self):
        """Numeric values with decimals are converted to float."""
        new_id = self._create('create Place latitude=37.77')
        obj = storage.all()["Place." + new_id]
        self.assertEqual(obj.latitude, 37.77)
        self.assertIsInstance(obj.latitude, float)

    def test_escaped_quote_param(self):
        """Escaped double quotes inside strings are unescaped."""
        new_id = self._create(r'create State name="Say_\"hi\""')
        obj = storage.all()["State." + new_id]
        self.assertEqual(obj.name, 'Say "hi"')

    def test_malformed_params_skipped(self):
        """Malformed parameters are skipped without failing creation."""
        new_id = self._create(
            'create State name="Cal" bad_param nonsense=12a3'
        )
        obj = storage.all()["State." + new_id]
        self.assertEqual(obj.name, "Cal")
        self.assertFalse(hasattr(obj, "bad_param"))
        self.assertFalse(hasattr(obj, "nonsense"))

    def test_missing_class(self):
        """Prints error when class name is missing."""
        output = self._create('create')
        self.assertEqual(output, "** class name missing **")

    def test_invalid_class(self):
        """Prints error when class name does not exist."""
        output = self._create('create FakeClass')
        self.assertEqual(output, "** class doesn't exist **")


if __name__ == "__main__":
    unittest.main()
