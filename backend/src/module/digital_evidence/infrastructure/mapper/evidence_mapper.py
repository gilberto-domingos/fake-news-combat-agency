from src.module.digital_evidence.domain.entity.evidence import Evidence
from src.module.digital_evidence.domain.entity.incident import Incident
from src.module.digital_evidence.infrastructure.model.evidence_model import EvidenceModel


class EvidenceMapper:
    @staticmethod
    def to_model(evidence: Evidence) -> EvidenceModel:
        return EvidenceModel(
            id=evidence.id,
            incident_id=evidence.incident.id,
            url=evidence.url,
            source=evidence.source,
            captured_at=evidence.captured_at,
            status=evidence.status,
            hash=evidence.hash,

        )

    @staticmethod
    def to_entity(model: EvidenceModel, incident: Incident) -> Evidence:
        evidence = Evidence(
            id=model.id,
            incident=incident,
            url=model.url,
            source=model.source,
            captured_at=model.captured_at,
            status=model.status,
            hash=model.hash,
        )

        return evidence
