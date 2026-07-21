from datetime import datetime
from uuid import UUID

from src.module.digital_evidence.domain.entity.incident import Incident
from src.module.digital_evidence.domain.enum.incident_status import IncidentStatus
from src.module.digital_evidence.domain.exception.business_exception import BusinessException
from src.module.digital_evidence.domain.repository_interface.incident_interface import IncidentInterface
from src.module.digital_evidence.domain.repository_interface.monitoring_target_interface import (
    MonitoringTargetInterface,
)


class IncidentCreateService:
    def __init__(
            self,
            incident_repository: IncidentInterface,
            monitoring_target_repository: MonitoringTargetInterface
    ):
        self._incident_repository = incident_repository
        self._monitoring_target_repository = monitoring_target_repository

    async def execute(
            self,
            monitoring_target_id: UUID,
            title: str,
            description: str,
    ) -> Incident:
        monitoring_target = await self._monitoring_target_repository.find_by_id(
            monitoring_target_id
        )

        if monitoring_target is None:
            raise BusinessException(
                message="Monitoring target id not found",
                error_code="MONITORING_TARGET_NOT_FOUND"
            )

        incident = Incident.create(
            monitoring_target_id=monitoring_target_id,
            title=title,
            description=description
        )

        await self._incident_repository.create(incident)

        return incident
