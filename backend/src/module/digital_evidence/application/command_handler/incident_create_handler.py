from src.module.digital_evidence.domain.entity.incident import Incident
from src.module.digital_evidence.domain.repository_interface.incident_interface import IncidentInterface
from src.module.digital_evidence.application.service_use_case.incident_create_service import IncidentCreateService
from src.module.digital_evidence.application.command.incident_create_cmd import IncidentCreateCommand


class IncidentCreateHandler:
    def __init__(self, service: IncidentCreateService):
        self._service = service

    async def handle(self, command: IncidentCreateCommand) -> Incident:
        incident = await self._service.execute(
            monitoring_target_id=command.monitoring_target_id,
            title=command.title,
            description=command.description,
        )
        return incident
