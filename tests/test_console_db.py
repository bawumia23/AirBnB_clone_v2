#!/usr/bin/python3
"""DB-mode console tests: each command must change the real tables."""
import os
import unittest
from io import StringIO
from unittest.mock import patch
import MySQLdb
from console import HBNBCommand


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db',
    "these tests need the database storage engine"
)
class TestConsoleCreateInDatabase(unittest.TestCase):
    """Check that console commands change the MySQL tables."""

    def _run(self, command):
        """Run a console command and return its stripped output."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(command)
        return output.getvalue().strip()

    def _query(self, sql, args=()):
        """Open a new MySQLdb connection and query the database."""
        db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor = db.cursor()
        cursor.execute(sql, args)
        rows = cursor.fetchall()
        cursor.close()
        db.close()
        return rows

    def _count(self, table):
        """Return the row count of the table via _query."""
        result = self._query("SELECT COUNT(*) FROM {}".format(table))
        return result[0][0]

    def test_create_state(self):
        """Count states, create a State, and assert count rose by 1."""
        initial_count = self._count('states')
        self._run('create State name="California"')
        final_count = self._count('states')
        self.assertEqual(final_count - initial_count, 1)

    def test_create_city_with_state(self):
        """Create a State, then a City linked to it, and check count."""
        state_id = self._run('create State name="California"')
        initial_count = self._count('cities')
        self._run('create City state_id="{}" name="Fremont"'.format(state_id))
        final_count = self._count('cities')
        self.assertEqual(final_count - initial_count, 1)

    def test_underscore_becomes_space(self):
        """Underscores in console arguments become spaces in the DB."""
        state_id = self._run('create State name="California"')
        city_id = self._run(
            'create City state_id="{}" name="San_Francisco"'.format(state_id)
        )
        rows = self._query("SELECT name FROM cities WHERE id = %s", (city_id,))
        self.assertEqual(rows[0][0], "San Francisco")
