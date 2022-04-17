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
    def quality_check(self, value):
        if value < 0:
            raise ValueError("quality cannot be negative.")
            
    @validator('name')
    def set_flags(self, value):
        if "aged" in value.lower():
            self.aged = True

    def update(self):
        if self.maxed is True:
            return
        
        if self.bottomed is True:
            return
        
        self.sell_in -= 1
        
        if self.quality == 0:
            return
        
        if self.backstage_passes is True:
            self.update_backstage_passes()
        
        if self.conjured is True:
            self.update_conjured()
        
        if self.aged is True:
            self.update_aged()

        if self.sell_in > 0:
            self.sell_in = self.sell_in - 1

    def update_conjured(self):
        return True
    
    def update_backstage_passes(self):
        return True
    
    def update_aged(self):
        if self.sell_in < 0:
            if self.quality + 4 >= 50:
                self.quality = 50
                self.maxed = True
                return
            elif self.quality + 4 < 50:
                self.quality += 4
        else:
            if self.quality + 2 >= 50:
                self.quality = 50
                self.maxed = True
                return 
            elif self.quality + 2 < 50:
                self.quality += 2
