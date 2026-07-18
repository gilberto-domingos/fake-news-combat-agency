from pydantic import BaseModel


class MonitoringTargetCreateDto(BaseModel):
    target_name: str
    keywords: list[str]
