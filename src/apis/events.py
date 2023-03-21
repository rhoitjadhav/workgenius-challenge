# Packages
import json
import copy
import redis
import websockets
from db.mongodb import get_database
from db.redisdb import get_redis_db
from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from motor.motor_asyncio import AsyncIOMotorClient
from websockets.exceptions import ConnectionClosedOK
from fastapi import WebSocket, Request, Depends, WebSocketDisconnect

# Modules
from usecases.events import EventsUsecase
from utils.ws_connection_manager import ConnectionManager

router = APIRouter()
manager = ConnectionManager()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def get(
        request: Request,
        redis_db: redis.Redis = Depends(get_redis_db),
        events_usecase: EventsUsecase = Depends(EventsUsecase),
):
    result = events_usecase.get(redis_db)
    return templates.TemplateResponse("index.html", {"request": request})


@router.websocket("/ws")
async def websocket_endpoint(
        websocket: WebSocket,
        db: AsyncIOMotorClient = Depends(get_database),
        redis_db: redis.Redis = Depends(get_redis_db),
        events_usecase: EventsUsecase = Depends(EventsUsecase),
):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            payload = json.loads(data)

            message = """"""
            for p in payload:
                if p.get("event"):
                    event = p["event"]
                    message += f"Email Status: {event}\n"

            # Adding to db and cache
            await events_usecase.add(db, copy.deepcopy(payload))
            events_usecase.add_to_cache(redis_db, copy.deepcopy(payload))
            await manager.broadcast(message)

    except (WebSocketDisconnect, ConnectionClosedOK):
        manager.disconnect(websocket)
        # await manager.broadcast(f"Client #{id(websocket)} left the chat")


@router.post("/callback")
async def callback(request: Request):
    form = await request.form()
    form_data = form.get("mandrill_events")

    async with websockets.connect("ws://localhost:8000/ws") as websocket:
        await websocket.send(form_data)

    return {"message": "Events Captured"}
