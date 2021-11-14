#!/usr/bin/python3

"""
test
"""

import unittest
import os
from models.base_model import BaseModel
import json

class TestBaseModel(unittest.TestCase):
    """
    testing the base model class
    """

    def setUp(self):
        self.model = BaseModel()
        return super().setUp()

    def tearDown(self):
        del(self.model)
        if os.path.exists('file.json'):
            os.remove('file.json')
        return super().tearDown()

    def test_instatiation(self):
        """
        checking whether self.model is an instance of BaseModel
        """
        self.assertIsInstance(self.model, BaseModel)


    def test_Dict_instance(self):
        """
        checking if instace give the correct output
        """
        dictModel = {
                      'my_number' : 89,
                      'name' : 'Holberton',
                      '__class__' : 'BaseModel',
                      'updated_at' : '2017-09-28T21:05:54.119572',
                      'id' : 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                      'created_at' : '2017-09-28T21:05:54.119427'
                     }
        myModel = BaseModel(**dictModel)
        self.assertIsInstance(myModel, BaseModel)
        self.assertEqual(myModel.my_number, 89)
        self.assertEqual(myModel.name, 'Holberton')
        self.assertEqual(myModel.id, 'b6a6e15c-c67d-4312-9a75-9d084935e579')

    def test_assignment(self):
        self.model.name = 'Holberton'
        self.model.my_number = 89
        self.assertIs(self.model.name, 'Holberton')
        self.assertIs(self.model.my_number, 89)

if __name__ == '__main__':
    unittest.main()
