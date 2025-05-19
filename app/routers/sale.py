from fastapi import APIRouter, Depends, Query , HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
from app.models.sale import Sale
from app.schemas.sale import SaleCreate, SaleOut
from app.database import SessionLocal
from sqlalchemy import func
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


## Add New Sale Route
@router.post("/", response_model=SaleOut)
def record_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    
    try:
        new_sale = Sale(**sale.dict())
        db.add(new_sale)
        db.commit()
        db.refresh(new_sale)
        return new_sale

    except Exception as e:
        logger.error(f"Error in adding sale record: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail='An unexpected error occurred.')


## Get Sale Summary Between Date Range Route
@router.get("/summary")
def sales_summary(
    db: Session = Depends(get_db),
    start_date: datetime = Query(...),
    end_date: datetime = Query(...)
):

    try:
        sales_data = db.query(
            func.date(Sale.sale_date).label("date"),
            func.sum(Sale.total_price).label("revenue")
        ).filter(
            Sale.sale_date >= start_date,
            Sale.sale_date <= end_date
        ).group_by(func.date(Sale.sale_date)).all()

        return [{"date": d.date, "revenue": d.revenue} for d in sales_data]
    
    except Exception as e:
        logger.error(f"Error in sales summary: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail='An unexpected error occurred.')


## Get Sale Comparison Between Two Date Range Route
@router.get("/comparison")
def revenue_comparison(
    db: Session = Depends(get_db),
    start_1: datetime = Query(...),
    end_1: datetime = Query(...),
    start_2: datetime = Query(...),
    end_2: datetime = Query(...)
):

    try:
        revenue_1 = db.query(func.sum(Sale.total_price)).filter(
            Sale.sale_date >= start_1,
            Sale.sale_date <= end_1
        ).scalar() or 0

        revenue_2 = db.query(func.sum(Sale.total_price)).filter(
            Sale.sale_date >= start_2,
            Sale.sale_date <= end_2
        ).scalar() or 0

        return {
            "period_1": {"start": start_1, "end": end_1, "revenue": revenue_1},
            "period_2": {"start": start_2, "end": end_2, "revenue": revenue_2},
            "difference": revenue_2 - revenue_1
        }
    
    except Exception as e:
        logger.error(f"Error in revenue comparison: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail='An unexpected error occurred.')
