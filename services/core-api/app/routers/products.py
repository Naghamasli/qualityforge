from fastapi import APIRouter, HTTPException
from app.schemas.product import Product


router = APIRouter(
    prefix="/api/products",
    tags=["Products"]
)


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


@router.get("", response_model=list[Product])
def get_products():
    return products


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )