from pydantic import BaseModel
from datetime import datetime

class InventoryUpdate(BaseModel):
    product_id: int
    stock_level: int

class InventoryOut(BaseModel):
    product_id: int
    stock_level: int
    updated_at: datetime

    class Config:
        orm_mode = True
