from fastapi import APIRouter
from src.module.digital_evidence.presentation.router.digital_evidence_router import router as evidence

api_router = APIRouter()

api_router.include_router(evidence)
