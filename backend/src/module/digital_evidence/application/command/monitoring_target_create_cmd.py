from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class MonitoringTargetCreateCommand:
    target_name: str
    keywords: list[str]
