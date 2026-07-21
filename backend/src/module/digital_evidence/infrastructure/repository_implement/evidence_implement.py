from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.module.digital_evidence.domain.entity.evidence import Evidence
from src.module.digital_evidence.domain.repository_interface.evidence_interface import EvidenceInterface
from src.module.digital_evidence.infrastructure.mapper.evidence_mapper import EvidenceMapper
from src.module.digital_evidence.infrastructure.model.evidence_model import EvidenceModel


class EvidenceImplement(EvidenceInterface):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, evidence: Evidence) -> Evidence:
        model = EvidenceMapper.to_model(evidence)

        self._session.add(model)
        await self._session.commit()

        return evidence

    async def find_by_id(self, evidence_id: UUID) -> Evidence | None:
        query = select(EvidenceModel).where(
            EvidenceModel.id == evidence_id
        )

        result = await self._session.execute(query)
        model: EvidenceModel | None = result.scalar_one_or_none()

        if model is None:
            return None

        return EvidenceMapper.to_entity(model)
