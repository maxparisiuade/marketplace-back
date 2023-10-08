from pydantic import BaseModel
from decimal import Decimal
from enum import Enum

class Category(str, Enum):
    food = "food"

class Product(BaseModel):
    uId: str
    name: str
    price: Decimal
    description: str
    image: str
    category: Category
    stock: int