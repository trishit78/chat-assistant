from sqlalchemy import text

from app.db.database import AsyncSessionLocal
from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/db-test")
async def db_test() -> dict[str, str]:
    async with AsyncSessionLocal() as session:
        result = await session.execute(text("SELECT 1"))
        one = result.scalar_one()
        return {"result": str(one)}
