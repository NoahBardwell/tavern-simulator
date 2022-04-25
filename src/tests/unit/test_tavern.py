import unittest
from tavern.item import Item
from tavern.tavern import Tavern

class TavernTest(unittest.TestCase):

    def test_one(self):
        item = Item.parse_obj(self.get_input_dict())
        print(item.dict())
        tavern = Tavern.parse_obj({"items": [item.dict()]})
        print(tavern)
        self.assertEqual(1, 1)
    
    def get_input_dict(self):
        return {"name":"Aged Cheese", "quality":5, "sell_in":3}