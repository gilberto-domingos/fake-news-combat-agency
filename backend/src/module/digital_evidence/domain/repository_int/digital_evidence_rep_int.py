from abc import ABC, abstractmethod
from src.module.digital_evidence.domain.entity.evidence import Evidence


class EvidenceRepository(ABC):
    @abstractmethod
    async def create(self, evidence: Evidence) -> Evidence:
        pass
