from fastapi import APIRouter
from src.module.digital_evidence.presentation.router.digital_evidence_router import router as evidence
from src.module.digital_evidence.presentation.router.monitoring_target_crt_router import router as monitoring_target
from src.module.digital_evidence.presentation.router.incident_crt_router_experiment import router as incident

api_router = APIRouter()

api_router.include_router(evidence)
api_router.include_router(monitoring_target)
api_router.include_router(incident)
