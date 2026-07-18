from src.module.digital_evidence.domain.entity.evidence import Evidence
from src.module.digital_evidence.domain.repository_interface.evidence_interface import EvidenceInterface
from src.module.digital_evidence.application.service_use_case.evidence_create_service import EvidenceCreateService
from src.module.digital_evidence.application.command.evidence_create_cmd import EvidenceCreateCommand


class EvidenceCreateHandler:
    def __init__(self, repository: EvidenceInterface, service: EvidenceCreateService):
        self._repository = repository
        self._service = service

    async def handle(self, command: EvidenceCreateCommand) -> Evidence:
        evidence = await self._service.execute(
            incident_id=command.incident_id,
            url=command.url,
            source=command.source,
        )
        return evidence
