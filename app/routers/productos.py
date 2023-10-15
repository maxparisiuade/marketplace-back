from fastapi import APIRouter
from ..db.db_service import DatabaseService
from ..models.productos import Producto

router = APIRouter()
router.tags=["productos"]

db_service_productos = DatabaseService('productos')
db_service_empresas = DatabaseService('empresas')

@router.get("/productos")
async def get_productos():
    return db_service_productos.get_all_items()

@router.get("/productos/empresa/{id_empresa}")
async def get_productos_de_empresa(id_empresa: str):
    empresa = db_service_empresas.get_item(id_empresa)
    if empresa:
        return empresa.productos
    return {"error": "Empresa not found"}

@router.get("/productos/{id}")
async def get_producto(id: str):
    producto = db_service_productos.get_item(id)
    if producto:
        return producto
    return {"error": "Producto not found"}

@router.post("/productos")
async def create_producto(producto: Producto):
    db_service_productos.add_item(producto)

@router.put("/productos/{id}")
async def update_producto(id: int, producto: Producto):
    db_service_productos.update_item(id, producto)
    return producto

@router.delete("/productos/{id}")
async def delete_producto(id: int):
    db_service_productos.delete_item(id)

