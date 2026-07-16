from src.module.digital_evidence.domain.entity.evidence import Evidence
from src.module.digital_evidence.domain.repository_int.digital_evidence_crt_int import DigitalEvidenceCrtInt
from src.module.digital_evidence.infrastructure.model.digital_evidence_model import DigitalEvidenceModel
from sqlalchemy.ext.asyncio import AsyncSession


class DigitalEvidenceImpl(DigitalEvidenceCrtInt):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, evidence: Evidence) -> Evidence:
        model = DigitalEvidenceModel(
            id=evidence.id,
            url=evidence.url,
            source=evidence.source,
            created_at=evidence.created_at,
            status=evidence.status,
            hash=evidence.hash
        )

        self.session.add(model)

        await self.session.commit()

        return evidence
