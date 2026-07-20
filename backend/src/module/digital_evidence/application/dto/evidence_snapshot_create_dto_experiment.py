from pydantic import BaseModel
from uuid import UUID


class EvidenceSnapshotCreateDto(BaseModel):
    evidence_id: UUID
    screenshot_path: str
    text_content: str
    html_path: str
    hash: str
