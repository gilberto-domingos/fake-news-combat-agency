from src.module.digital_evidence.domain.entity.evidence import Evidence
from abc import ABC, abstractmethod
from uuid import UUID


class EvidenceReadInterface(ABC):
    @abstractmethod
    async def find_by_id(self, evidence_id: UUID) -> Evidence | None:
        pass
