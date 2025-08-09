from fastapi import APIRouter

router = APIRouter()

@router.get("/proyectos")
def listar_proyectos():
    return {"mensaje": "Lista de proyectos"}
