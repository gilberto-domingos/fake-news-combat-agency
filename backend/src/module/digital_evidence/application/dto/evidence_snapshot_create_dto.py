from pydantic import BaseModel


class EvidenceSnapshotCreateDto(BaseModel):
    screenshot_path: str
    text_content: str
    html_path: str
    hash: str
