import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from filestorage import FileStorage
import json
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_storage._FileStorage__file_path):
            os.remove(self.file_storage._FileStorage__file_path)

    def test_add_obj(self):
        obj = BaseModel()
        self.file_storage.add_obj(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertTrue(key in self.file_storage.retrieve())

    def test_save_and_retrieve(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.file_storage.add_obj(obj1)
        self.file_storage.add_obj(obj2)
        self.file_storage.save()
        retrieved_objs = self.file_storage.retrieve()
        self.assertTrue(len(retrieved_objs) == 2)

    def test_deserialize(self):
        obj = BaseModel()
        self.file_storage.add_obj(obj)
        self.file_storage.save()
        self.file_storage = FileStorage()
        self.file_storage.deserialize()
        self.assertTrue(len(self.file_storage.retrieve()) == 1)

    @patch('json.load')
    @patch('builtins.open')
    def test_deserialize_exception(self, mock_open, mock_load):
        mock_open.side_effect = FileNotFoundError
        self.file_storage.deserialize()
        self.assertEqual(len(self.file_storage.retrieve()), 0)

    @patch('json.dump')
    @patch('builtins.open')
    def test_save_exception(self, mock_open, mock_dump):
        mock_open.side_effect = FileNotFoundError
        obj = BaseModel()
        self.file_storage.add_obj(obj)
        self.file_storage.save()
        self.assertFalse(os.path.exists(self.file_storage._FileStorage__file_path))


if __name__ == '__main__':
    unittest.main()
