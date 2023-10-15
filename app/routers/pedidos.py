from fastapi import APIRouter
from ..db.db_service import DatabaseService
from ..models.pedidos import Pedido

router = APIRouter()
router.tags=["pedidos"]

db_service_pedidos = DatabaseService('pedidos')
db_service_usuarios = DatabaseService('usuarios')
db_service_empresas = DatabaseService('empresas')

@router.get("/pedidos")
async def get_pedidos():
    return db_service_pedidos.get_all_items()

@router.get("/pedidos/usuario/{id_usuario}")
async def get_pedidos_de_usuario(id_usuario: str):
    usuario = db_service_usuarios.get_item(id_usuario)
    if usuario:
        return usuario.pedidos
    return {"error": "Usuario not found"}

@router.get("/pedidos/empresa/{id_empresa}")
async def get_pedidos_de_empresas(id_empresa: str):
    empresa = db_service_empresas.get_item(id_empresa)
    if empresa:
        return empresa.pedidos
    return {"error": "Empresa not found"}

@router.get("/pedidos/{id}")
async def get_pedido(id: str):
    pedido = db_service_pedidos.get_item(id)
    if pedido:
        return pedido
    return {"error": "Pedido not found"}

@router.post("/pedidos")
async def create_pedido(pedido: Pedido):
    db_service_pedidos.add_item(pedido)

@router.put("/pedidos/{id}")
async def update_pedido(id: int, product: Pedido):
    db_service_pedidos.update_item(id, product)
    return product

@router.delete("/pedidos/{id}")
async def delete_pedido(id: int):
    db_service_pedidos.delete_item(id)

