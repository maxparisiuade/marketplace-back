from fastapi import FastAPI
from mangum import Mangum

from app.routers import users, products

app = FastAPI()
app.include_router(users.router)
app.include_router(products.router)

handler = Mangum(app)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}