from src.module.digital_evidence.domain.entity.evidence import Evidence
from src.module.digital_evidence.infrastructure.model.evidence_model import EvidenceModel


class EvidenceMapper:

    @staticmethod
    def to_model(evidence: Evidence) -> EvidenceModel:
        model = EvidenceModel(
            id=evidence.id,
            incident_id=evidence.incident_id,
            url=evidence.url,
            source=evidence.source,
            captured_at=evidence.captured_at,
            status=evidence.status,
            hash=evidence.hash,
        )
        return model

    @staticmethod
    def to_entity(model: EvidenceModel) -> Evidence:
        entity = Evidence.from_persistence(
            id=model.id,
            incident_id=model.incident_id,
            url=model.url,
            source=model.source,
            captured_at=model.captured_at,
            status=model.status,
            hash=model.hash,
        )
        return entity
