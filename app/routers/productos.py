from fastapi import APIRouter
from ..db.db_service import DatabaseService
from ..models.productos import Producto, Rubro, Categoria, get_subcategorias_de_rubro

router = APIRouter()
router.tags=["productos"]

db_service_productos = DatabaseService('productos')
db_service_empresas = DatabaseService('empresas')

@router.get("/productos")
async def get_productos():
    return db_service_productos.get_all_items()

@router.get("/productos/rubro/{rubro}")
async def get_productos_por_rubro(rubro: str):
    productos = db_service_productos.get_all_items()
    productos_rubro = []
    for producto in productos:
        if producto["rubro"] == rubro:
            productos_rubro.append(producto)
    return productos_rubro

@router.get("/productos/categoria/{categoria}")
async def get_productos_por_categoria(categoria: str):
    productos = db_service_productos.get_all_items()
    productos_categoria = []
    for producto in productos:
        if producto["categoria"] == categoria:
            productos_categoria.append(producto)
    return productos_categoria

@router.get("/productos/rubro")
async def get_all_rubros():
    return list(Rubro)

@router.get("/productos/rubro/{rubro}/categoria")
async def get_categorias_de_rubro(rubro: str):
    return get_subcategorias_de_rubro(rubro)

@router.get("/productos/empresa/{id_empresa}")
async def get_productos_de_empresa(id_empresa: str):
    empresa = db_service_empresas.get_item(id_empresa)
    if empresa:
        return empresa["productos"]
    return {"error": "Empresa not found"}

@router.get("/productos/{id}")
async def get_producto(id: str):
    producto = db_service_productos.get_item(id)
    if producto:
        return producto
    return {"error": "Producto not found"}

@router.post("/productos")
async def create_producto(producto: Producto):
    empresa = db_service_empresas.get_item(producto.id_empresa)
    empresa["productos"].append(producto.dict())
    db_service_empresas.update_item(producto.id_empresa, empresa)
    db_service_productos.add_item(producto)

@router.put("/productos/{id}")
async def update_producto(id: int, producto: Producto):
    db_service_productos.update_item(id, producto)
    return producto

@router.delete("/productos/{id}")
async def delete_producto(id: int):
    producto = db_service_productos.get_item(id)
    empresa = db_service_empresas.get_item(producto["id_empresa"])
    empresa["productos"].remove(producto)
    db_service_empresas.update_item(producto["id_empresa"], empresa)
    db_service_productos.delete_item(id)

