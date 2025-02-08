from fastapi import WebSocket
from .db import get_db

async def traffic_websocket(websocket: WebSocket):
    await websocket.accept()
    while True:
        db = await get_db()
        row = await db.fetchrow("SELECT * FROM traffic_data ORDER BY timestamp DESC LIMIT 1")
        await db.close()
        if row:
            await websocket.send_json({"zona": row["zona"], "nivel": row["nivel"]})
