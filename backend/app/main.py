from fastapi import FastAPI
from .routes import router
from .websockets import traffic_websocket, alerts_websocket

app = FastAPI()

app.include_router(router)
app.websocket("/ws/traffic")(traffic_websocket)
app.websocket("/ws/alerts")(alerts_websocket)
