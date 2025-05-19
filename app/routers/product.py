from fastapi import APIRouter, Depends , HTTPException
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, ProductOut
from app.models.product import Product
from app.database import SessionLocal
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


## Product Create Route
@router.post("/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):

    try:
        db_product = Product(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    except Exception as e:
        logger.error(f"Error in product create: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail='An unexpected error occurred.')