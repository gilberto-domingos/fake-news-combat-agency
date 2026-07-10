from src.module.digital_evidence.application.service_use_case.monitoring_target_crt_service import \
    MonitoringTargetCreateService
from src.module.digital_evidence.application.command.monitoring_target_crt_cmd import MonitoringTargetCrtCommand
from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget


class MonitoringTargetHandler:
    def __init__(self, service: MonitoringTargetCreateService):
        self._service = service
    
    async def handle(self, command: MonitoringTargetCrtCommand) -> MonitoringTarget:
        create = await self._service.execute(
            target_name=command.target_name,
            keywords=command.keywords,
            is_active=command.is_active,
            created_at=command.created_at
        )

        return create
