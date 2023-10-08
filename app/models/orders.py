from pydantic import BaseModel
from typing import List

from .products import Product

class Order(BaseModel):
    uId: str
    timestamp: int
    total: float
    delivery_time: int
    products: List[Product] = []