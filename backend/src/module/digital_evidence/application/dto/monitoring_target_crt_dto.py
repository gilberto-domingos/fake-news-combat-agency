from pydantic import BaseModel


class MonitoringTargetCrtDto(BaseModel):
    target_name: str
    keywords: list[str]
