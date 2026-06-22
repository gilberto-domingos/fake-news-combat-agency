from fastapi import APIRouter

from src.module.land.presentation.router.router_registry import api_router as land_router
from src.module.digital_evidence.presentation.router.router_registry import api_router as digital_evidence_router

api_router = APIRouter()

api_router.include_router(land_router)
api_router.include_router(digital_evidence_router)
