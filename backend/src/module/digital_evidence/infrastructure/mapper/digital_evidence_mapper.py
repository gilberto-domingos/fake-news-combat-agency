from src.module.digital_evidence.domain.entity.evidence import Evidence
from src.module.digital_evidence.domain.enum.evidence_status import EvidenceStatus
from src.module.digital_evidence.infrastructure.model.digital_evidence_model import DigitalEvidenceModel


class EvidenceMapper:

    @staticmethod
    def to_model(evidence: Evidence) -> DigitalEvidenceModel:
        return DigitalEvidenceModel(
            id=evidence.id,
            url=evidence.url,
            source=evidence.source,
            captured_at=evidence.captured_at,
            status=evidence.status,
            hash=evidence.hash
        )

    @staticmethod
    def to_entity(model: DigitalEvidenceModel) -> Evidence:
        evidence = Evidence(
            id=model.id,
            url=model.url,
            source=model.source
        )

        evidence._captured_at = model.captured_at
        evidence._status = EvidenceStatus(model.status)
        evidence._hash = model.hash

        return evidence
