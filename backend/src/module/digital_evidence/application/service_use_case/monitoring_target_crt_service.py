from datetime import datetime
from src.module.digital_evidence.domain.repository_int.monitoring_target_rep_int import MonitoringTargetRepInt
from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget


# Use Case service
class MonitoringTargetCreateService:
    def __init__(self, repository: MonitoringTargetRepInt):
        self._repository = repository

    async def execute(self,
                      target_name: str,
                      keywords: list[str],
                      is_active: bool,
                      created_at: datetime
                      ) -> MonitoringTarget:
        monitoring_target = MonitoringTarget(
            target_name=target_name,
            keywords=keywords,
            is_active=is_active,
            created_at=created_at
        )
        await self._repository.create(monitoring_target)
        return monitoring_target
