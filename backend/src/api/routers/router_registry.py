from fastapi import APIRouter
from src.api.routers.auth_router import router as auth
from src.api.routers.analytics_access_router import router as counter_access
from src.api.routers.invest_router import router as invest

api_router = APIRouter()

api_router.include_router(auth)
api_router.include_router(counter_access)
api_router.include_router(invest)
