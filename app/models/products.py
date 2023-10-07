from pydantic import BaseModel

class Product(BaseModel):
    uId: str
    name: str
    mercado: str