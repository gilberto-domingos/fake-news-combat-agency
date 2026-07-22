# -> Validate snapshots, # -> Validate integrity, # -> Compare hashes

from src.module.digital_evidence.domain.entity.evidence import Evidence


class EvidenceSnapshotIntegrityPolicyService:

    def is_valid_for_processing(self, evidence: Evidence) -> bool:
        if not evidence.url:
            return False

        if not evidence.source:
            return False

        return True
