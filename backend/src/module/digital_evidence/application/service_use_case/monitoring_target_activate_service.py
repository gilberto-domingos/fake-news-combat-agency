from uuid import UUID
from src.module.digital_evidence.domain.repository_interface.monitoring_target_write_interface import \
    MonitoringTargetRepositoryInt
from src.module.digital_evidence.domain.exception.business_exception import BusinessException


class MonitoringTargetActivateService:
    def __init__(self, repository: MonitoringTargetRepositoryInt):
        self._repository = repository

    async def execute(self, monitoring_target_id: UUID):
        monitoring_target = await self._repository.find_by_id(monitoring_target_id)

        if monitoring_target is None:
            raise BusinessException(
                message="Monitoring Target not found",
                error_code="MONITORING_TARGET_NOT_FOUND"
            )

        if monitoring_target.is_active:
            raise BusinessException(
                message="Monitoring Target already active",
                error_code="MONITORING_TARGET_ALREADY_ACTIVE"
            )
        monitoring_target.activate()
        await self._repository.update(monitoring_target)
