from pydantic import BaseModel, Field


class EvidenceCrtDto(BaseModel):
    url: str
    source: str
