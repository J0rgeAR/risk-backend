from fastapi import APIRouter

router = APIRouter()

@router.get("/riesgos/ping")
async def ping_riesgos():
    return {"message": "pong from riesgos"}
