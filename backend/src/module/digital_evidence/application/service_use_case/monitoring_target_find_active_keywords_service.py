from src.module.digital_evidence.domain.repository_interface.monitoring_target_read_interface import \
    MonitoringTargetReadInterface


class MonitoringTargetFindActiveKeywordsService:
    def __init__(self, repository: MonitoringTargetReadInterface):
        self._repository = repository

    async def execute(self, keywords: list[str], is_active: bool) -> list[list[str]]:
        result = await self._repository.find_active_keywords(
            keywords=keywords,
            is_active=is_active
        )
        return result
