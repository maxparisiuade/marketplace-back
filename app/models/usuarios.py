from pydantic import BaseModel
from typing import List

from .pedidos import Pedido
from ..utils.utils import generate_short_unique_id

class Usuario(BaseModel):
    uId: str = generate_short_unique_id()
    nombre: str
    apellido: str
    dni: int
    email: str
    celular: str = ""
    direccion: str
    pedidos: List[dict] = []