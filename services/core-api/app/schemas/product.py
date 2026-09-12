from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class Product(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: Decimal
    stock: int