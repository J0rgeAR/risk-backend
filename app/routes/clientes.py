from fastapi import APIRouter

router = APIRouter()

@router.get("/users/ping")
async def ping_users():
    return {"message": "pong from users"}
