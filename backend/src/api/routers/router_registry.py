from fastapi import APIRouter
from src.api.routers.auth_router import router as auth
from src.api.routers.access_counter_router import router as counter_access

api_router = APIRouter()

api_router.include_router(auth)
api_router.include_router(counter_access)
