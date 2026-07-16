from src.module.digital_evidence.domain.entity.evidence import Evidence
from src.module.digital_evidence.domain.repository_int.digital_evidence_crt_int import DigitalEvidenceRepositoryInt
from src.module.digital_evidence.application.command.digital_evidence_crt_cmd import DigitalEvidenceCrtCommand


class DigitalEvidenceHandler:
    def __init__(self, repository: DigitalEvidenceRepositoryInt):
        self.repository = repository

    async def handle(self, command: DigitalEvidenceCrtCommand, metadata: dict | None = None):
        evidence = Evidence.create(
            url=command.url,
            source=command.source,
        )

        return await self.repository.create(evidence)
