from fastapi import APIRouter
from .db import get_db

router = APIRouter()

@router.get("/traffic")
async def get_traffic():
    db = await get_db()
    rows = await db.fetch("SELECT * FROM traffic_data ORDER BY timestamp DESC LIMIT 10")
    await db.close()
    return rows
