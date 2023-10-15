from pydantic import BaseModel
from typing import List

from .productos import Producto
from .pedidos import Pedido

from enum import Enum

class Rubro(str, Enum):
    ELECTRONICA_TECNOLOGIA = "Electrónica y Tecnología"
    HOGAR = "Hogar"
    ALIMENTOS_BEBIDAS = "Alimentos y Bebidas"
    SALUD_BELLEZA = "Salud y Belleza"
    MODA_ROPA = "Moda y Ropa"

class Empresa(BaseModel):
    uId: str
    razon_social: str
    cuit: str
    email: str = ""
    celular: str = ""
    direccion: str
    url: str
    color_primario: str
    color_secundario: str
    logo_svg: str
    rubro: Rubro
    productos: List[Producto] = []
    pedidos: List[Pedido] = []