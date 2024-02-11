#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_attributes_initialization(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_setters(self):
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_to_dict(self):
        user_dict = self.user.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("__class__", user_dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["email"], "")
        self.assertEqual(user_dict["password"], "")
        self.assertEqual(user_dict["first_name"], "")
        self.assertEqual(user_dict["last_name"], "")


if __name__ == "__main__":
    unittest.main()
