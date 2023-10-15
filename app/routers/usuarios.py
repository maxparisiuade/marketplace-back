from fastapi import APIRouter
from ..db.db_service import DatabaseService
from ..models.usuarios import Usuario

router = APIRouter()
router.tags=["usuarios"]

db_service = DatabaseService('usuarios')

@router.get("/usuarios")
async def get_usuarios():
    return db_service.get_all_items()

@router.get("/usuarios/{id}")
async def get_usuario(id: str):
    usuario = db_service.get_item(id)
    if usuario:
        return usuario
    return {"error": "User not found"}

@router.post("/usuarios")
async def create_usuario(usuario: Usuario):
    db_service.add_item(usuario)

@router.put("/usuarios/{id}")
async def update_usuario(id: int, product: Usuario):
    db_service.update_item(id, product)
    return product

@router.delete("/usuarios/{id}")
async def delete_usuario(id: int):
    db_service.delete_item(id)

