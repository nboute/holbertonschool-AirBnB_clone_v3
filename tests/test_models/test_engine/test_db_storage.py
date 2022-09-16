#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_method_no_args(self):
        """test with No cls and no id"""
        state = models.storage.get(None, None)
        self.assertEqual(None, state)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get(self):
        """test with no valid id"""
        state = State(name='Louisiana')
        state.save()
        user = User(first_name="John", last_name="Mc Clane",
                    email="die@hard.com", password="Hans Gruber")
        user.save()
        self.assertIs(state, models.storage.get(State, state.id))
        self.assertIs(user, models.storage.get(User, user.id))

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_method_no_id(self):
        """test with no valid id"""
        state = models.storage.get(State, "rqhqerhq454543")
        self.assertEqual(None, state)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_method_no_id_state(self):
        """test with no valid id"""
        state = models.storage.get(State, "rqhqerhq454543")
        self.assertEqual(None, state)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_method_no_id_user(self):
        """test with no valid id"""
        user = models.storage.get(User, "rqhqerhq454543")
        self.assertEqual(None, user)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_method_no_id_place(self):
        """test with no valid id"""
        place = models.storage.get(Place, "rqhqerhq454543")
        self.assertEqual(None, place)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_method_no_id_amenity(self):
        """test with no valid id"""
        amenity = models.storage.get(Amenity, "rqhqerhq454543")
        self.assertEqual(None, amenity)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_method_no_id_city(self):
        """test with no valid id"""
        city = models.storage.get(City, "rqhqerhq454543")
        self.assertEqual(None, city)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get_method_all_states(self):
        """test id for all states"""
        states = models.storage.all(State)
        for state in states.values():
            test_state = models.storage.get(State, state.id)
            self.assertEqual(state.name, test_state.name)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count(self):
        """test count all object in a class"""
        all = models.storage.all()
        count_all = models.storage.count()
        self.assertEqual(count_all, len(all))

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count_method_all(self):
        """test count all objects"""
        all = models.storage.all()
        count_all = models.storage.count()
        self.assertEqual(count_all, len(all))

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count_method_state(self):
        """test count for state class"""
        all_state = models.storage.all(State)
        count_state = models.storage.count(State)
        self.assertEqual(count_state, len(all_state))
