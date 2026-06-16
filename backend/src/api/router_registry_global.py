from fastapi import APIRouter

from src.module.land.presentation.router.router_registry import api_router as land_router

api_router = APIRouter()

api_router.include_router(land_router)
