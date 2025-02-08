import asyncpg

DATABASE_URL = "postgresql://user:password@db/traffic_db"

async def get_db():
    return await asyncpg.connect(DATABASE_URL)
