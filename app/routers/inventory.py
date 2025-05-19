from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models.inventory import Inventory
from app.schemas.inventory import InventoryOut, InventoryUpdate
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


## Low Stock Route
@router.get("/low-stock", response_model=List[InventoryOut])
def get_low_stock_items(db: Session = Depends(get_db), threshold: int = 10):

    try:
        items = db.query(Inventory).filter(Inventory.stock_level <= threshold).all()
        return items

    except Exception as e:
        logger.error(f"Error in inventory low-stock: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail='An unexpected error occurred.')


## Inventory Update Route
@router.put("/update", response_model=InventoryOut)
def update_inventory(data: InventoryUpdate, db: Session = Depends(get_db)):

    try:
        inv = db.query(Inventory).filter(Inventory.product_id == data.product_id).first()
        if not inv:
            raise HTTPException(status_code=404, detail="Inventory entry not found")

        inv.stock_level = data.stock_level
        db.commit()
        db.refresh(inv)
        return inv

    except Exception as e:
        logger.error(f"Error in inventory update: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail='An unexpected error occurred.')
