from pydantic import BaseModel
from datetime import datetime

class SaleCreate(BaseModel):
    product_id: int
    quantity: int
    total_price: float

class SaleOut(SaleCreate):
    id: int
    sale_date: datetime

    class Config:
        orm_mode = True
