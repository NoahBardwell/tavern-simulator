import unittest
from item import Item
from inventory import Inventory


class TavernTest(unittest.TestCase):

    def test_one(self):
        item = Item.parse_obj(self.get_input_dict())
        print(item.dict())
        inventory = Inventory.parse_obj({"items": [item.dict()]})
        print(inventory)
        self.assertEqual(1, 1)

    def get_input_dict(self):
        return {"name": "Aged Cheese", "quality": 5, "sell_in": 3}
