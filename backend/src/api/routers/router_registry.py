from fastapi import APIRouter
from src.api.routers.user_router import router as users
from src.api.routers.auth_router import router as auth_router
from src.api.routers.user_router import router as counter_access

api_router = APIRouter()

api_router.include_router(users)
api_router.include_router(auth_router)
api_router.include_router(counter_access)
