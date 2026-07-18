from src.module.digital_evidence.domain.entity.evidence import Evidence
from src.module.digital_evidence.domain.repository_interface.evidence_interface import EvidenceInterface
from src.module.digital_evidence.infrastructure.model.evidence_model import DigitalEvidenceModel
from sqlalchemy.ext.asyncio import AsyncSession


class EvidenceImplement(EvidenceInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, evidence: Evidence) -> Evidence:
        model = DigitalEvidenceModel(
            id=evidence.id,
            url=evidence.url,
            source=evidence.source,
            captured_at=evidence.captured_at,
            status=evidence.status,
            hash=evidence.hash
        )
        self.session.add(model)
        await self.session.commit()
        return evidence
