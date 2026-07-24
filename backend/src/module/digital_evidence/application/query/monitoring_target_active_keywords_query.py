from dataclasses import dataclass


@dataclass(frozen=True)
class MonitoringTargetActiveKeywordsQuery:
    keywords: list[str]
    is_active: bool
