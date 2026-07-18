from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class MonitoringTargetCrtCommand:
    target_name: str
    keywords: list[str]
    is_active: bool
    created_at: datetime
