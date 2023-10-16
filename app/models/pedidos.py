from decimal import Decimal
from pydantic import BaseModel
from typing import List
import time
from ..utils.utils import generate_short_unique_id

from .productos import Producto

from enum import Enum

class EstadoPedido(str, Enum):
    PENDIENTE = "PENDIENTE"
    EN_PROCESO = "EN PROCESO"
    EN_CAMINO = "EN CAMINO"
    ENTREGADO = "ENTREGADO"
    CANCELADO = "CANCELADO"

class Pedido(BaseModel):
    uId: str = generate_short_unique_id()
    fecha_pedido: int = int(time.time())
    fecha_entrega: int = 0
    total: Decimal
    tiempo_delivery: int
    productos: List[dict] = []
    pagado: bool
    estado: EstadoPedido

class PedidoInput(BaseModel):
    total: Decimal
    tiempo_delivery: int
    id_productos: List[str] = []
    id_usuario: str
    id_empresa: str
    pagado: bool
    estado: EstadoPedido = EstadoPedido.PENDIENTE

class PedidoUpdate(BaseModel):
    pagado: bool | None = None
    estado: EstadoPedido | None = None