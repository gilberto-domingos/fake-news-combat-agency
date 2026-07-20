from fastapi import APIRouter
from src.module.digital_evidence.presentation.router.monitoring_target_create_router import router as monitoring_target
from src.module.digital_evidence.presentation.router.incident_create_router_experiment import router as incident
from src.module.digital_evidence.presentation.router.evidence_create_router_experiment import router as evidence
from src.module.digital_evidence.presentation.router.evidence_snapshot_create_router_experiment import \
    router as evidence_snapshot

api_router = APIRouter()

api_router.include_router(monitoring_target)
api_router.include_router(incident)
api_router.include_router(evidence)
api_router.include_router(evidence_snapshot)
