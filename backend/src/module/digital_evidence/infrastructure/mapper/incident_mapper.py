from src.module.digital_evidence.domain.entity.incident import Incident
from src.module.digital_evidence.infrastructure.model.incident_model import IncidentModel


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
    def to_entity(
            model: IncidentModel
    ) -> Incident:
        entity = Incident.from_persistence(
            id=model.id,
            monitoring_target_id=model.monitoring_target_id,
            title=model.title,
            description=model.description,
            status=model.status,
            created_at=model.created_at
        )
        return entity
