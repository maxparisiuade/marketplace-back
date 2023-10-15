from decimal import Decimal
from pydantic import BaseModel
from typing import List

from .productos import Producto

from enum import Enum

class EstadoPedido(str, Enum):
    PENDIENTE = "CREADO"
    EN_PROCESO = "EN PROCESO"
    EN_CAMINO = "EN CAMINO"
    ENTREGADO = "ENTREGADO"
    CANCELADO = "CANCELADO"

class Pedido(BaseModel):
    uId: str
    fecha_pedido: int  #timestamp
    fecha_entrega: int  #timestamp
    total: Decimal
    tiempo_delivery: int
    productos: List[Producto] = []
    pagado: bool
    estado: EstadoPedido