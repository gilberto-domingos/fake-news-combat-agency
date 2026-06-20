from src.module.digital_evidence.domain.service.evidence_service import EvidenceService
from src.module.digital_evidence.application.command.digital_evidence_crt_comm import DigitalEvidenceCrtCommand


class DigitalEvidenceHandler:
    def __init__(self, evidence_service: EvidenceService):
        self.evidence_service = evidence_service

    async def handle(self, command: DigitalEvidenceCrtCommand):
        response = await self.evidence_service.create(
            url=command.url,
            source=command.source
        )
        return response
