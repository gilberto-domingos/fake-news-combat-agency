from src.module.digital_evidence.application.command.evidence_snapshot_create_cmd import EvidenceSnapshotCreateCommand
from src.module.digital_evidence.application.service_use_case.evidence_snapshot_create_service import \
    EvidenceSnapshotCreateService
from src.module.digital_evidence.domain.entity.evidence_snapshot import \
    EvidenceSnapshot


class EvidenceSnapshotCreateHandler():
    def __init__(self, service: EvidenceSnapshotCreateService):
        self._service = service

    async def handle(self, command: EvidenceSnapshotCreateCommand) -> EvidenceSnapshot:
        evidence_snapshot = await self._service.execute(
            evidence_id=command.evidence_id,
            screenshot_path=command.screenshot_path,
            text_content=command.text_content,
            html_path=command.html_path,
            hash=command.hash
        )
        return evidence_snapshot
