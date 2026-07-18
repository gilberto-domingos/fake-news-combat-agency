from abc import ABC, abstractmethod
from src.module.digital_evidence.domain.entity.evidence import Evidence


class EvidenceInterface(ABC):
    @abstractmethod
    async def create(self, evidence: Evidence) -> Evidence:
        pass
