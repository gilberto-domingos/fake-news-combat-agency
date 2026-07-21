from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class EvidenceSnapshotCreateCommand:
    evidence_id: UUID
    screenshot_path: str
    text_content: str
    html_path: str
    hash: str
