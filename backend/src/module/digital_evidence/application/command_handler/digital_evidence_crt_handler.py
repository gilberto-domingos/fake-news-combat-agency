from uuid import uuid4
from datetime import datetime, UTC

import hashlib
from src.module.digital_evidence.domain.enum.evidence_status import EvidenceStatus
from src.module.digital_evidence.domain.entity.evidence import Evidence
from src.module.digital_evidence.domain.repository_int.digital_evidence_rep_int import DigitalEvidenceRepositoryInt
from src.module.digital_evidence.application.command.digital_evidence_crt_comm import DigitalEvidenceCrtCommand


class DigitalEvidenceHandler:
    def __init__(self, repository: DigitalEvidenceRepositoryInt):
        self.repository = repository

    async def handle(self, command: DigitalEvidenceCrtCommand):
        evidence = Evidence(
            id=uuid4(),
            url=command.url,
            source=command.source,
            captured_at=datetime.now(UTC),
            status=EvidenceStatus.CAPTURED,
            hash=hashlib.sha256(f"{command.url}:{command.source}:{datetime.now(timezone.utc)}".encode()).hexdigest()
        )

        return await self.repository.create(evidence)
