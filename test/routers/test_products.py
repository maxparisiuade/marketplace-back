import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json()["name"] == "apple"

def test_get_nonexistent_product():
    response = client.get("/products/3")
    assert response.status_code == 200
    assert response.json()["error"] == "Product not found"

def test_create_product():
    product = {"name": "orange", "price": 15, "id": 3}
    response = client.post("/products", json=product)
    assert response.status_code == 200
    assert response.json() == product

def test_update_product():
    product = {"name": "banana", "price": 25, "id": 2}
    response = client.put("/products/2", json=product)
    assert response.status_code == 200
    assert response.json() == product

def test_delete_product():
    response = client.delete("/products/2")
    assert response.status_code == 200
    assert response.json()["message"] == "Product deleted successfully"