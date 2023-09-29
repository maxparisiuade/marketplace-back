from fastapi import APIRouter
from ..models.products import Product

router = APIRouter()

products = [
        {"name": "apple", "price": 10, "id": 1},
        {"name": "banana", "price": 20, "id": 2},
    ]

@router.get("/products", tags=["products"])
async def get_products():
    return products

@router.get("/products/{product_id}", tags=["products"])
async def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}

@router.post("/products", tags=["products"])
async def create_product(product: Product):
    return product

@router.put("/products/{product_id}", tags=["products"])
async def update_product(product_id: int, product: Product):
    return product

@router.delete("/products/{product_id}", tags=["products"])
async def delete_product(product_id: int):
    return {"message": "Product deleted successfully"}
    