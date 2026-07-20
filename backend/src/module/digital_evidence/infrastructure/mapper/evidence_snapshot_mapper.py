from src.module.digital_evidence.domain.entity.evidence_snapshot import EvidenceSnapshot
from src.module.digital_evidence.domain.entity.evidence import Evidence
from src.module.digital_evidence.infrastructure.model.evidence_snapshot_model import EvidenceSnapshotModel
from src.module.digital_evidence.infrastructure.mapper.evidence_mapper import EvidenceMapper


class EvidenceSnapshotMapper:
    @staticmethod
    def to_model(evidence_snapshot: EvidenceSnapshot) -> EvidenceSnapshotModel:
        model = EvidenceSnapshotModel(
            id=evidence_snapshot.id,
            evidence_id=evidence_snapshot.evidence.id,
            text_content=evidence_snapshot.text_content,
            html_path=evidence_snapshot.html_path,
            screenshot_path=evidence_snapshot.screenshot_path,
            hash=evidence_snapshot.hash,
            captured_at=evidence_snapshot.captured_at
        )
        return model

    @staticmethod
    def to_entity(model: EvidenceSnapshotModel) -> EvidenceSnapshot:
        entity = EvidenceSnapshot(
            evidence=EvidenceMapper.to_entity(model.evidence),
            text_content=model.text_content,
            html_path=model.html_path,
            screenshot_path=model.screenshot_path,
            hash=model.hash,
            captured_at=model.captured_at
        )
        return entity
