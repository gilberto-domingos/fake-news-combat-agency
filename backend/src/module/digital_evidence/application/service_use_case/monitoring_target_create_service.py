from datetime import datetime
from src.module.digital_evidence.domain.repository_interface.monitoring_target_interface import \
    MonitoringTargetInterface
from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget


class MonitoringTargetCreateService:
    def __init__(self, repository: MonitoringTargetInterface):
        self._repository = repository

    async def execute(self,
                      target_name: str,
                      keywords: list[str],
                      ) -> MonitoringTarget:
        monitoring_target = MonitoringTarget.create(
            target_name=target_name,
            keywords=keywords,
            is_active=True,
            created_at=datetime.now()
        )
        await self._repository.create(monitoring_target)
        return monitoring_target
