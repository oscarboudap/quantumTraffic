from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import asyncpg
import json

app = FastAPI()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración de la base de datos
DATABASE_URL = "postgresql://user:password@db:5432/traffic_db"

async def fetch_traffic_data():
    conn = await asyncpg.connect(DATABASE_URL)
    rows = await conn.fetch("SELECT zona, lat, lon, nivel FROM traffic")
    await conn.close()
    return [{"zona": r["zona"], "lat": r["lat"], "lon": r["lon"], "nivel": r["nivel"]} for r in rows]

@app.get("/traffic")
async def get_traffic():
    return await fetch_traffic_data()

# WebSocket para datos en tiempo real
@app.websocket("/ws/traffic")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        traffic_data = await fetch_traffic_data()
        await websocket.send_text(json.dumps(traffic_data))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)