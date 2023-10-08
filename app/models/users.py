from pydantic import BaseModel
from typing import List

from .orders import Order

class User(BaseModel):
    uId: str
    name: str
    address: str
    phone: str
    orders: List[Order] = []