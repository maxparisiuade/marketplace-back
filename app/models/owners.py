from pydantic import BaseModel
from typing import List

from .products import Product
from .orders import Order

class Owner(BaseModel):
    uId: str
    company_name: str
    address: str
    phone: str
    url: str
    primary_color: str
    secondary_color: str
    logo: str
    products: List[Product] = []
    active_orders: List[Order] = []