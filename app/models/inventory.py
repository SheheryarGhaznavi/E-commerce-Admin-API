from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), unique=True, nullable=False)
    stock_level = Column(Integer, nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    product = relationship("Product")
