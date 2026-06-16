from fastapi import APIRouter
from src.module.land.presentation.router.auth_router import router as auth
from src.module.land.presentation.router.invest_router import router as invest
from src.module.land.presentation.router.analytics_access_router import router as analytics_access

api_router = APIRouter()

api_router.include_router(auth)
api_router.include_router(invest)
api_router.include_router(analytics_access)
