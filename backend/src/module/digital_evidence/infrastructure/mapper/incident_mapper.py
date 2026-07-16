from src.module.digital_evidence.domain.entity.incident import Incident
from src.module.digital_evidence.infrastructure.model.incident_model import IncidentModel
from src.module.digital_evidence.infrastructure.mapper.monitoring_target_mapper import MonitoringTargetMapper


class IncidentMapper:

    @staticmethod
    def to_model(incident: Incident) -> IncidentModel:
        model = IncidentModel(
            id=incident.id,
            monitoring_target_id=incident.monitoring_target_id,
            title=incident.title,
            description=incident.description,
            status=incident.status,
            created_at=incident.created_at
        )
        return model

    @staticmethod
    def to_entity(model: IncidentModel) -> Incident:
        entity = Incident(
            monitoring_target=MonitoringTargetMapper.to_entity(model.monitoring_target),
            title=model.title,
            description=model.description,
            status=model.status,
            created_at=model.created_at
        )
        return entity
