from src.module.digital_evidence.domain.repository_interface.monitoring_target_write_interface import \
    MonitoringTargetWriteInterface
from src.module.digital_evidence.domain.repository_interface.monitoring_target_read_interface import \
    MonitoringTargetReadInterface
from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget
from src.module.digital_evidence.infrastructure.mapper.monitoring_target_mapper import MonitoringTargetMapper
from src.module.digital_evidence.infrastructure.model.monitoring_target_model import MonitoringTargetModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID


class MonitoringTargetImplement(MonitoringTargetWriteInterface, MonitoringTargetReadInterface):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, monitoring_target: MonitoringTarget) -> MonitoringTarget:
        model = MonitoringTargetMapper.to_model(monitoring_target)

        self._session.add(model)

        await self._session.commit()

        return monitoring_target

    async def find_by_id(self, monitoring_target_id: UUID) -> MonitoringTarget | None:
        query = select(MonitoringTargetModel).where(MonitoringTargetModel.id == monitoring_target_id)

        result = await self._session.execute(query)

        model: MonitoringTargetModel | None = result.scalar_one_or_none()

        if model is None:
            return None

        return MonitoringTargetMapper.to_entity(model)

    async def find_active_keywords(self, keywords: list[str], is_active: bool) -> list[list[str]]:
        query = select(MonitoringTargetModel.keywords).where(MonitoringTargetModel.is_active == is_active)

        result = await self._session.execute(query)

        active_keywords: list[list[str]] = list(result.scalars().all())

        return active_keywords

    """ 
    async def update(self, monitoring_target: MonitoringTarget) -> None:
        model = MonitoringTargetMapper.to_model(monitoring_target)

        await self._session.merge(model)

        await self._session.commit()

    async def delete(self, monitoring_target_id: UUID) -> None:
        query = select(MonitoringTargetModel).where(MonitoringTargetModel.id == monitoring_target_id)

        result = await self._session.execute(query)

        model: MonitoringTargetModel | None = result.scalar_one_or_none()

        if model is not None:
            await self._session.delete(model)

            await self._session.commit()
"""
