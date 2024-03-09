#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """A test case class for testing the functionality of the BaseModel class."""
    def test_init(self):
        """Test the initialization of a BaseModel instance."""
        base_model = BaseModel()
        self.assertIsNone(base_model.id)
        self.assertIsNone(base_model.created_at)
        self.assertIsNone(base_model.updated_at)

    def test_save(self):
        """Test the saving functionality of the BaseModel class."""
        base_model = BaseModel()
        my_instance = BaseModel()
        my_instance.save()
        self.assertTrue(True)

        with self.assertRaises(NotImplementedError):
        base_model.save()

    def test_delete(self):
        """Test the deletion functionality of the BaseModel class."""
        base_model = BaseModel()
        my_instance = BaseModel()
        my_instance.delete()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
