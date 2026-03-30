from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.core.config import settings
from app.db.database import engine

app = FastAPI(title="AI Project Assistant")

app.include_router(health_router)


@app.on_event("shutdown")
async def shutdown() -> None:
    await engine.dispose()


@app.get("/hello")
def root() -> dict[str, str]:
    return {"message": f"{settings.app_name} is running"}
