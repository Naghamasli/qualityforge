from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="ShopForge Core API",
    version="0.1.0"
)


class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int


products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 1200.0,
        "stock": 5
    },
    {
        "id": 2,
        "name": "Keyboard",
        "price": 80.0,
        "stock": 12
    },
    {
        "id": 3,
        "name": "Mouse",
        "price": 40.0,
        "stock": 20
    }
]
@app.get("/api/products", response_model=list[Product])
def get_products():
    return products


@app.get("/api/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )