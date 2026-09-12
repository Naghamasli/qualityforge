from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.product import ProductModel
from app.schemas.product import Product


router = APIRouter(
    prefix="/api/products",
    tags=["Products"]
)


@router.get("", response_model=list[Product])
def get_products(db: Session = Depends(get_db)):
    statement = select(ProductModel)
    products = db.scalars(statement).all()

    return products


@router.get("/{product_id}", response_model=Product)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.get(ProductModel, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product