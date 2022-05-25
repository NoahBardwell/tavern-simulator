import unittest
from item import Item
from inventory import Inventory


class TavernTest(unittest.TestCase):

    def test_one(self):
        item = Item.parse_obj(self.get_input_dict())
        print(item.dict())
        inventory = Inventory.parse_obj({"items": [item.dict()]})
        inventory.update()
        print(inventory)
        self.assertEqual(inventory.items[0].sell_in, 2)
        self.assertEqual(inventory.items[0].quality, 7)

    def get_input_dict(self):
        return {"name": "Aged Cheese", "quality": 5, "sell_in": 3}
