from src.module.digital_evidence.domain.repository_interface.incident_interface import IncidentInterface
from src.module.digital_evidence.domain.entity.incident import Incident
from src.module.digital_evidence.infrastructure.mapper.incident_mapper import IncidentMapper
from src.module.digital_evidence.infrastructure.model.incident_model import IncidentModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID


class IncidentImplement(IncidentInterface):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, incident: Incident) -> Incident:
        model = IncidentMapper.to_model(incident)

        self._session.add(model)
        await self._session.commit()
        return incident

    async def find_by_id(self, incident_id: UUID) -> Incident | None:
        query = select(IncidentModel).where(IncidentModel.id == incident_id)

        result = await self._session.execute(query)
        model: IncidentModel | None = result.scalar_one_or_none()

        if model is None:
            return None

        return IncidentMapper.to_entity(model)
