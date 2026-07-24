from abc import ABC, abstractmethod
from src.module.digital_evidence.domain.entity.evidence_snapshot import EvidenceSnapshot


class EvidenceSnapshotWriteInterface(ABC):
    @abstractmethod
    async def create(self, evidence_snapshot: EvidenceSnapshot) -> EvidenceSnapshot:
        pass
