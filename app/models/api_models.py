from pydantic import BaseModel
from typing import Optional, List


    
class ItemNutrient(BaseModel):
    name: str
    amount: Optional[float]

class Item(BaseModel):
    name: str
    category: str
    cook_type: Optional[str] = None
    protein: Optional[float] = None
    carbs: Optional[float] = None
    fat: Optional[float] = None
    weight: Optional[float] = None
    portion: Optional[str] = None
    nutrients: Optional[List[ItemNutrient]] = None
    
class ItemList(BaseModel):
    items: List[dict]
    
