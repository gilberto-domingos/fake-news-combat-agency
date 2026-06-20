from src.module.digital_evidence.domain.entity.evidence import Evidence
from src.module.digital_evidence.domain.repository_int.digital_evidence_rep_int import EvidenceRepository


class EvidenceService:
    def __init__(self, repository: EvidenceRepository):
        self.repository = repository

    async def create(self, url: str, source: str) -> Evidence:
        evidence = Evidence(url=url, source=source)

        return await self.repository.create(evidence)
