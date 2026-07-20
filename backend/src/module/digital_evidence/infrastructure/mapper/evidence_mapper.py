from src.module.digital_evidence.domain.entity.evidence import Evidence
from src.module.digital_evidence.domain.entity.incident import Incident
from src.module.digital_evidence.infrastructure.model.evidence_model import EvidenceModel
from src.module.digital_evidence.infrastructure.mapper.incident_mapper import IncidentMapper


class EvidenceMapper:
    @staticmethod
    def to_model(evidence: Evidence) -> EvidenceModel:
        model = EvidenceModel(
            id=evidence.id,
            incident_id=evidence.incident.id,
            url=evidence.url,
            source=evidence.source,
            captured_at=evidence.captured_at,
            status=evidence.status,
            hash=evidence.hash,
        )
        return model

    @staticmethod
    def to_entity(model: EvidenceModel) -> Evidence:
        entity = Evidence(
            id=model.id,
            incident=IncidentMapper.to_entity(model.incident),
            url=model.url,
            source=model.source,
            captured_at=model.captured_at,
            status=model.status,
            hash=model.hash,
        )
        return entity

# evidence=EvidenceMapper.to_entity(model.evidence),
