from pydantic import BaseModel
from typing import List
from item import Item


class Tavern(BaseModel):
    items: List[Item]
