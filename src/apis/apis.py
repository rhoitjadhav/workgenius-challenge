# Packages
from fastapi import APIRouter

# Modules
from .events import router as events

router = APIRouter()

router.include_router(events)
