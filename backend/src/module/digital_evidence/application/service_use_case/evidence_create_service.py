from src.module.digital_evidence.domain.repository_interface.evidence_interface import EvidenceInterface
from src.module.digital_evidence.domain.repository_interface.incident_interface import IncidentInterface
from src.module.digital_evidence.domain.entity.evidence import Evidence
from src.module.digital_evidence.domain.exception.business_exception import BusinessException
from src.module.digital_evidence.domain.enum.evidence_status import EvidenceStatus
from uuid import UUID
from datetime import datetime


class EvidenceCreateService():
    def __init__(self, repository_evidence: EvidenceInterface, repository_incident: IncidentInterface):
        self._repository_evidence = repository_evidence
        self._repository_incident = repository_incident

    async def execute(self,
                      incident_id: UUID,
                      url: str,
                      source: str,
                      status: EvidenceStatus,
                      hash: str
                      ) -> Evidence:
        incident = await self._repository_incident.find_by_id(incident_id)

        if incident is None:
            raise BusinessException(
                message="Incident id not found",
                error_code="INCIDENT_NOT_FOUND"
            )

        entity = Evidence.create(
            incident=incident,
            url=url,
            source=source,
            hash=hash,
        )
        await self._repository_evidence.create(entity)

        return entity
