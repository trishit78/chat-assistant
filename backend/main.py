from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.core.config import settings
from app.db.database import db

app = FastAPI(title="AI Project Assistant")

app.include_router(health_router)

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()



@app.get("/hello")
def root():
    return {
        "message": f"{settings.database_url} is running"
    }