from src.module.digital_evidence.domain.entity.incident import Incident
from src.module.digital_evidence.domain.repository_int.incident_rep_int import IncidentRepositoryCrtInt
from src.module.digital_evidence.application.service_use_case.incident_crt_service import IncidentCrtService
from src.module.digital_evidence.application.command.incident_crt_cmd import IncidentCrtCommand


class IncidentCrtHandler:
    def __init__(self, service: IncidentCrtService, repository: IncidentRepositoryCrtInt):
        self._service = service
        self._repository = repository

    async def handle(self, command: IncidentCrtCommand) -> Incident:
        incident = await self._service.execute(
            monitoring_target_id=command.monitoring_target_id,
            title=command.title,
            description=command.description,
        )
        return incident
