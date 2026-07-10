from src.module.digital_evidence.domain.repository_int.monitoring_target_rep_int import MonitoringTargetRepInt
from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget
from src.module.digital_evidence.infrastructure.model.monitoring_target_model import MonitoringTargetModel
from sqlalchemy.ext.asyncio import AsyncSession


class MonitoringTargetImpl(MonitoringTargetRepInt):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, monitoring_target: MonitoringTarget) -> MonitoringTarget:
        model = MonitoringTargetModel(
            id=monitoring_target.id,
            target_name=monitoring_target.target_name,
            keywords=monitoring_target.keywords,
            is_active=monitoring_target.is_active,
            created_at=monitoring_target.created_at
        )
        self._session.add(model)

        await self._session.commit()

        return monitoring_target
