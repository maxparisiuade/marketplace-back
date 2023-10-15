from fastapi import FastAPI
from mangum import Mangum

from app.routers import productos, usuarios

app = FastAPI()
app.include_router(usuarios.router)
app.include_router(productos.router)

handler = Mangum(app)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}