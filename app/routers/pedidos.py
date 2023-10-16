from fastapi import APIRouter
from ..db.db_service import DatabaseService
from ..models.pedidos import Pedido, PedidoInput, PedidoUpdate

router = APIRouter()
router.tags=["pedidos"]

db_service_pedidos = DatabaseService('pedidos')
db_service_usuarios = DatabaseService('usuarios')
db_service_empresas = DatabaseService('empresas')
db_service_productos = DatabaseService('productos')

@router.get("/pedidos")
async def get_pedidos():
    return db_service_pedidos.get_all_items()

@router.get("/pedidos/usuario/{id_usuario}")
async def get_pedidos_de_usuario(id_usuario: str):
    usuario = db_service_usuarios.get_item(id_usuario)
    if usuario:
        return usuario["pedidos"]
    return {"error": "Usuario not found"}

@router.get("/pedidos/empresa/{id_empresa}")
async def get_pedidos_de_empresas(id_empresa: str):
    empresa = db_service_empresas.get_item(id_empresa)
    if empresa:
        return empresa["pedidos"]
    return {"error": "Empresa not found"}

@router.get("/pedidos/{id}")
async def get_pedido(id: str):
    pedido = db_service_pedidos.get_item(id)
    if pedido:
        return pedido
    return {"error": "Pedido not found"}

@router.post("/pedidos")
async def create_pedido(pedido_intput: PedidoInput):
    pedido = Pedido(**pedido_intput.dict())
    pedido.fecha_entrega = pedido.fecha_pedido + pedido.tiempo_delivery
    for id_producto in pedido_intput.id_productos:
        producto = db_service_productos.get_item(id_producto)
        if producto:
            pedido.productos.append(producto)

    usuario = db_service_usuarios.get_item(pedido_intput.id_usuario)
    empresa = db_service_empresas.get_item(pedido_intput.id_empresa)

    usuario["pedidos"].append(pedido.dict())
    empresa["pedidos"].append(pedido.dict())

    db_service_usuarios.update_item(usuario['uId'], usuario)
    db_service_empresas.update_item(empresa['uId'], empresa)
    db_service_pedidos.add_item(pedido)

@router.put("/pedidos/{id}")
async def update_pedido(id: int, pedido_update: PedidoUpdate):
    pedido = db_service_pedidos.get_item(id)
    if pedido_update.pagado is not None:
        pedido['pagado'] = pedido_update.pagado
    if pedido_update.estado is not None:
        pedido['estado'] = pedido_update.estado
    db_service_pedidos.update_item(id, pedido)

@router.delete("/pedidos/{id}")
async def delete_pedido(id: int):
    db_service_pedidos.delete_item(id)

