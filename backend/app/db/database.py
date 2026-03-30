import asyncpg
from app.core.config import settings

class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(
            dsn=settings.database_url
        )

    async def disconnect(self):
       # if self.pool is not None:
            await self.pool.close()
         #   self.pool = None

db = Database()