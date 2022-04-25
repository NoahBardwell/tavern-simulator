import unittest
from tavern.item import Item
from tavern.tavern import Tavern

class TavernTest(unittest.TestCase):

    def test_one(self):
        Item.parse_obj(self.get_input_dict())
        self.assertEqual(1, 1)
    
    def get_input_dict(self):
        return {"test":"test"}