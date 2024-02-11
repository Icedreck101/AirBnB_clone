#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_init(self):
        """
        Test the initialization of a BaseModel instance.
        """
        my_model = BaseModel()

        # Ensure id, created_at, and updated_at are not None
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        Test the save method of the BaseModel class.
        """
        my_model = BaseModel()

        # Record the initial updated_at timestamp
        first_updated_at = my_model.updated_at

        # Call save method to update the updated_at timestamp
        my_model.save()
        current_updated_at = my_model.updated_at

        # Ensure the updated_at timestamp has changed
        self.assertNotEqual(first_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the BaseModel class.
        """
        my_model = BaseModel()

        # Convert BaseModel instance to dictionary
        my_model_dict = my_model.to_dict()

        # Ensure the returned object is a dictionary
        self.assertIsInstance(my_model_dict, dict)

        # Check keys and values in the dictionary
        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(my_model_dict["created_at"], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.updated_at.isoformat())

    def test_str(self):
        """
        Test the __str__ method of the BaseModel class.
        """
        my_model = BaseModel()

        # Ensure the string representation starts with '[BaseModel]'
        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        # Ensure the BaseModel id is present in the string representation
        self.assertIn(my_model.id, str(my_model))

        # Ensure the BaseModel's __dict__ is present in the string representation
        self.assertIn(str(my_model.__dict__), str(my_model))

if __name__ == "__main__":
    unittest.main()
