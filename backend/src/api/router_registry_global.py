from fastapi import APIRouter

from src.module.land.presentation.router.router_registry import api_router as land_router
from src.module.digital_evidence.presentation.router.router_registry import api_router as evidence_router
from src.module.digital_evidence.presentation.router.router_registry import api_router as incident
from src.module.digital_evidence.presentation.router.router_registry import api_router as evidence_snapshot

api_router = APIRouter()

api_router.include_router(land_router)
api_router.include_router(evidence_router)
api_router.include_router(incident)
api_router.include_router(evidence_snapshot)
