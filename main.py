from fastapi import FastAPI
from mangum import Mangum

from app.routers import productos, usuarios, empresas, pedidos

app = FastAPI()
app.include_router(usuarios.router)
app.include_router(productos.router)
app.include_router(empresas.router)
app.include_router(pedidos.router)

handler = Mangum(app)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}