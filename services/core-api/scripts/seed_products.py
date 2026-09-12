from decimal import Decimal

from sqlalchemy import select

from app.database import SessionLocal
from app.models.product import ProductModel


def seed_products():
    db = SessionLocal()

    try:
        existing_product = db.scalar(
            select(ProductModel).limit(1)
        )

        if existing_product:
            print("Products already exist. Skipping seed.")
            return

        products = [
            ProductModel(
                name="Laptop",
                price=Decimal("1200.00"),
                stock=5
            ),
            ProductModel(
                name="Keyboard",
                price=Decimal("80.00"),
                stock=12
            ),
            ProductModel(
                name="Mouse",
                price=Decimal("40.00"),
                stock=20
            )
        ]

        db.add_all(products)
        db.commit()

        print("Products seeded successfully!")

    finally:
        db.close()


if __name__ == "__main__":
    seed_products()