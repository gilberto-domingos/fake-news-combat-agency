from abc import ABC, abstractmethod
from uuid import UUID
from src.module.digital_evidence.domain.entity.evidence import Evidence


class EvidenceWriteInterface(ABC):
    @abstractmethod
    async def create(self, evidence: Evidence) -> Evidence:
        pass

    @abstractmethod
    async def find_by_id(self, evidence_id: UUID) -> Evidence | None:
        pass
