from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class EvidenceSnapshotResponseDto(BaseModel):
    id: UUID
    evidence_id: UUID
    screenshot_path: str
    hash: str
    text_content: str
    html_path: str
    captured_at: datetime
