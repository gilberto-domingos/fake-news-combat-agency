from src.module.digital_evidence.application.service_use_case.monitoring_target_create_service import \
    MonitoringTargetCreateService
from src.module.digital_evidence.application.command.monitoring_target_create_cmd import MonitoringTargetCreateCommand
from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget


class MonitoringTargetCreateHandler:
    def __init__(self, service: MonitoringTargetCreateService):
        self._service = service

    async def handle(self, command: MonitoringTargetCreateCommand) -> MonitoringTarget:
        create = await self._service.execute(
            target_name=command.target_name,
            keywords=command.keywords,
        )

        return create
