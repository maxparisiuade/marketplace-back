from fastapi import FastAPI
import uvicorn

from .routers import users, products

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}