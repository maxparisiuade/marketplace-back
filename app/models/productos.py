from pydantic import BaseModel
from decimal import Decimal
from enum import Enum
from typing import List
from ..utils.utils import generate_short_unique_id

class Rubro(str, Enum):
    MODA_ROPA = "Moda y ropa"
    ELECTRONICA_TECNOLOGIA = "Electrónica y tecnología"
    ALIMENTACION_BEBIDAS = "Alimentación y bebidas"
    SALUD_BELLEZA = "Salud y belleza"
    HOGAR = "Hogar"

class Categoria(str, Enum):
    ROPA_HOMBRE = "Ropa de hombre"
    ROPA_MUJER = "Ropa de mujer"
    ROPA_INFANTIL = "Ropa infantil"
    CALZADO = "Calzado"
    ACCESORIOS = "Accesorios"
    TELEFONOS_MOVILES = "Teléfonos móviles"
    PEQUEÑOS_DISPOSITIVOS = "Pequeños dispositivos"
    ACCESORIOS_ELECTRONICOS = "Accesorios electrónicos"
    AUDIO_SONIDO = "Audio y sonido"
    VIDEOJUEGOS = "Videojuegos"
    FRUTAS_VERDURAS = "Frutas y verduras"
    CARNES_PESCADOS = "Carnes y pescados"
    PRODUCTOS_LACTEOS = "Productos lácteos"
    BEBIDAS = "Bebidas"
    SNACKS_DULCES = "Snacks y dulces"
    CUIDADO_PIEL_MAQUILLAJE = "Cuidado de la piel/Maquillaje"
    CUIDADO_CABELLO = "Cuidado del cabello"
    HIGIENE_PERSONAL = "Productos de higiene personal"
    PERFUMES_FRAGANCIAS = "Perfumes y fragancias"
    CUIDADO_DENTAL = "Cuidado dental"
    DECORACION_HOGAR = "Decoración del hogar"
    ELECTRODOMESTICOS_PEQUEÑOS = "Electrodomésticos pequeños"
    UTENSILIOS_COCINA = "Utensilios de cocina"
    ILUMINACION = "Iluminación"

rubro_subcategorias = {
    Rubro.MODA_ROPA: [
        Categoria.ROPA_HOMBRE,
        Categoria.ROPA_MUJER,
        Categoria.ROPA_INFANTIL,
        Categoria.CALZADO,
        Categoria.ACCESORIOS,
    ],
    Rubro.ELECTRONICA_TECNOLOGIA: [
        Categoria.TELEFONOS_MOVILES,
        Categoria.PEQUEÑOS_DISPOSITIVOS,
        Categoria.ACCESORIOS_ELECTRONICOS,
        Categoria.AUDIO_SONIDO,
        Categoria.VIDEOJUEGOS,
    ],
    Rubro.ALIMENTACION_BEBIDAS: [
        Categoria.FRUTAS_VERDURAS,
        Categoria.CARNES_PESCADOS,
        Categoria.PRODUCTOS_LACTEOS,
        Categoria.BEBIDAS,
        Categoria.SNACKS_DULCES,
    ],
    Rubro.SALUD_BELLEZA: [
        Categoria.CUIDADO_PIEL_MAQUILLAJE,
        Categoria.CUIDADO_CABELLO,
        Categoria.HIGIENE_PERSONAL,
        Categoria.PERFUMES_FRAGANCIAS,
        Categoria.CUIDADO_DENTAL,
    ],
    Rubro.HOGAR: [
        Categoria.DECORACION_HOGAR,
        Categoria.ELECTRODOMESTICOS_PEQUEÑOS,
        Categoria.UTENSILIOS_COCINA,
        Categoria.ILUMINACION,
    ],
}

def get_subcategorias_de_rubro(rubro: Rubro) -> List[Categoria]:
    return rubro_subcategorias.get(rubro, [])

class Producto(BaseModel):
    uId: str = generate_short_unique_id()
    titulo: str
    marca: str
    precio: Decimal
    id_empresa: str
    description: str
    imagen: str
    stock: bool
    nro_stock: int
    rubro: Rubro
    categoria: Categoria