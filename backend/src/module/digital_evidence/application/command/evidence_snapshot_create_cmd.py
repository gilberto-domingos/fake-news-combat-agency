from dataclasses import dataclass


@dataclass(frozen=True)
class EvidenceSnapshotCreateCommand:
    screenshot_path: str
    text_content: str
    html_path: str
    hash: str
