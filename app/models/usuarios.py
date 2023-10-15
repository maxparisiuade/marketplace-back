from pydantic import BaseModel
from typing import List

from .pedidos import Pedido

class Usuario(BaseModel):
    uId: str
    nombre: str
    apellido: str
    dni: int
    email: str
    celular: str = ""
    direccion: str
    pedidos: List[Pedido] = []