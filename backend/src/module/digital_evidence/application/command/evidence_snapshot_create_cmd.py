from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class EvidenceSnapshotCreateCommand:
    screenshot_path: str
    text_content: str
    html_path: str
    hash: str
