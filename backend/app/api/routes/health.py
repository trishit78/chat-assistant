from app.db.database import db
from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/")
def health_check():
    return {"status": "ok"}

@router.get("/db-test")
async def db_test():
    async with db.pool.acquire() as conn:
        result = await conn.fetch("SELECT 1;")
        return {"result": str(result)}