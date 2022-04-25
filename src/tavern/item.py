from pydantic import BaseModel, validator, constr
from typing import Optional

class Item(BaseModel):
    name: constr(min_length=1)
    sell_in: int
    quality: int
    legendary: Optional[bool] = False
    backstage_passes: Optional[bool] = False
    conjured: Optional[bool] = False
    aged: Optional[bool] = False
    maxed: Optional[bool] = False
    bottomed: Optional[bool] = False

    @validator('quality')
    def quality_check(cls, value):
        if value < 0:
            raise ValueError("quality cannot be negative.")
            
    @validator('name')
    def set_flags(cls, value):
        if "aged" in value.lower():
            cls.aged = True

    def update(cls):
        if cls.maxed is True:
            return
        
        if cls.bottomed is True:
            return
        
        cls.sell_in -= 1
        
        if cls.quality == 0:
            return
        
        if cls.backstage_passes is True:
            cls.update_backstage_passes()
        
        if cls.conjured is True:
            cls.update_conjured()
        
        if cls.aged is True:
            cls.update_aged()

        if cls.sell_in > 0:
            cls.sell_in = cls.sell_in - 1

    def update_conjured(cls):
        return True
    
    def update_backstage_passes(cls):
        return True
    
    def update_aged(cls):
        if cls.sell_in < 0:
            if cls.quality + 4 >= 50:
                cls.quality = 50
                cls.maxed = True
                return
            elif cls.quality + 4 < 50:
                cls.quality += 4
        else:
            if cls.quality + 2 >= 50:
                cls.quality = 50
                cls.maxed = True
                return 
            elif cls.quality + 2 < 50:
                cls.quality += 2
