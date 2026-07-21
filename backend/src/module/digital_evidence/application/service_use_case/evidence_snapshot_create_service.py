from uuid import UUID

from src.module.digital_evidence.domain.entity.evidence_snapshot import EvidenceSnapshot
from src.module.digital_evidence.domain.exception.business_exception import BusinessException
from src.module.digital_evidence.domain.repository_interface.evidence_interface import EvidenceInterface
from src.module.digital_evidence.domain.repository_interface.evidence_snapshot_interface import (
    EvidenceSnapshotInterface
)


class EvidenceSnapshotCreateService:

    def __init__(
            self,
            repository_evidence_snapshot: EvidenceSnapshotInterface,
            repository_evidence: EvidenceInterface
    ):
        self._repository_evidence_snapshot = repository_evidence_snapshot
        self._repository_evidence = repository_evidence

    async def execute(
            self,
            evidence_id: UUID,
            screenshot_path: str,
            text_content: str,
            html_path: str,
            hash: str
    ) -> EvidenceSnapshot:
        evidence = await self._repository_evidence.find_by_id(
            evidence_id
        )

        if evidence is None:
            raise BusinessException(
                message="Id evidence not found",
                error_code="ID_EVIDENCE_NOT_FOUND"
            )

        evidence_snapshot = EvidenceSnapshot.create(
            evidence_id=evidence_id,
            screenshot_path=screenshot_path,
            text_content=text_content,
            html_path=html_path,
            hash=hash,
        )

        await self._repository_evidence_snapshot.create(
            evidence_snapshot
        )

        return evidence_snapshot
