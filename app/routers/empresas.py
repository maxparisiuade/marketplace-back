from fastapi import APIRouter
from ..db.db_service import DatabaseService
from ..models.empresas import Empresa

router = APIRouter()
router.tags=["empresas"]

db_service = DatabaseService('empresas')

@router.get("/empresas")
async def get_empresas():
    return db_service.get_all_items()

@router.get("/empresas/{id}")
async def get_empresa(id: str):
    empresa = db_service.get_item(id)
    if empresa:
        return empresa
    return {"error": "Empresa not found"}

@router.post("/empresas")
async def create_empresa(empresa: Empresa):
    db_service.add_item(empresa)

@router.put("/empresas/{id}")
async def update_empresa(id: int, empresa: Empresa):
    db_service.update_item(id, empresa)
    return empresa

@router.delete("/empresas/{id}")
async def delete_empresa(id: int):
    db_service.delete_item(id)