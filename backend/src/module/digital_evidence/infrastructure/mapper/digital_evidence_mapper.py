from src.module.digital_evidence.domain.entity.evidence import Evidence
from src.module.digital_evidence.domain.entity.incident import Incident
from src.module.digital_evidence.infrastructure.model.digital_evidence_model import DigitalEvidenceModel


class EvidenceMapper:

    @staticmethod
    def to_model(evidence: Evidence) -> DigitalEvidenceModel:
        return DigitalEvidenceModel(
            id=evidence.id,
            incident_id=evidence.incident.id,
            url=evidence.url,
            source=evidence.source,
            created_at=evidence.created_at,
            status=evidence.status,
            hash=evidence.hash,

        )

    @staticmethod
    def to_entity(model: DigitalEvidenceModel, incident: Incident) -> Evidence:
        evidence = Evidence(
            id=model.id,
            incident=incident,
            url=model.url,
            source=model.source,
            created_at=model.created_at,
            status=model.status,
            hash=model.hash,
            snapshots=[]
        )

        return evidence
