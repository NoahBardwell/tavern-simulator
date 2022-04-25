from pydantic import BaseModel
from typing import List
from tavern.item import Item


class Tavern(BaseModel):
    items: List[Item]

    def update(cls):
        for item in cls.items:
            item.update()
