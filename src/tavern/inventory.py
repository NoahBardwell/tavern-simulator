from pydantic import BaseModel
from typing import List
from item import Item


class Inventory(BaseModel):
    items: List[Item]

    def update(cls):
        for item in cls.items:
            item.update()
