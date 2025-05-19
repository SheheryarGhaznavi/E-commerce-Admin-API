from fastapi import FastAPI
from app.routers import product, sale, inventory

app = FastAPI()

app.include_router(product.router, prefix="/products", tags=["Products"])
app.include_router(sale.router, prefix="/sales", tags=["Sales"])
app.include_router(inventory.router, prefix="/inventory", tags=["Inventory"])

@app.get("/")
def root():
    return {"message": "E-commerce Admin API"}