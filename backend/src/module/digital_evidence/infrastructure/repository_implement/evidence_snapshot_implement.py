from src.module.digital_evidence.domain.repository_interface.evidence_snapshot_interface import \
    EvidenceSnapshotInterface
from sqlalchemy.ext.asyncio import AsyncSession
from src.module.digital_evidence.domain.entity.evidence_snapshot import EvidenceSnapshot
from src.module.digital_evidence.infrastructure.mapper.evidence_snapshot_mapper import EvidenceSnapshotMapper


class EvidenceSnapshotImplement(EvidenceSnapshotInterface):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, evidence_snapshot: EvidenceSnapshot) -> EvidenceSnapshot:
        model = EvidenceSnapshotMapper.to_model(evidence_snapshot)
        self._session.add(model)
        await self._session.commit()
        return evidence_snapshot
