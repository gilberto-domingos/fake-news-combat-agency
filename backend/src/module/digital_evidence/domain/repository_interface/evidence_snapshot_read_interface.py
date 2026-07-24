from abc import ABC, abstractmethod
from src.module.digital_evidence.domain.entity.evidence_snapshot import EvidenceSnapshot
from uuid import UUID


class EvidenceSnapshotReadInterface(ABC):
    @abstractmethod
    async def find_all(self, evidence_snapshot: EvidenceSnapshot) -> EvidenceSnapshot:
        pass

    @abstractmethod
    async def find_by_id(self, id: UUID) -> EvidenceSnapshot | None:
        pass
