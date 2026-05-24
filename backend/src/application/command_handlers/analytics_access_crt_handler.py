from src.application.command.analytics_access_crt_cmm import AnalyticsAccessCreateCommand, RequestMetadata
from src.domain.entities.analytics_access import AnalyticsAccess
from src.domain.repositories_int.analytics_access_rep_int import AnalyticsAccessRepositoryInt
from uuid import uuid4


class AnalyticsAccessCreateHandler:
    def __init__(self, analytics_access_repository: AnalyticsAccessRepositoryInt):
        self.repository = analytics_access_repository

    async def handle(self, command: AnalyticsAccessCreateCommand,
                     metadata: RequestMetadata | None = None) -> AnalyticsAccess:
        analytics = AnalyticsAccess(
            id=uuid4(),
            route=command.route,
            timestamp=command.timestamp,
            user_agent=command.user_agent,
            language=command.language,
            platform=command.platform,
            screen_width=command.screen_width,
            screen_height=command.screen_height,
            timezone=command.timezone,
            sessionId=command.sessionId,
            fingerprint=command.fingerprint,
            ip_address=metadata.ip_address,
            country=metadata.country,
            bot_detection=metadata.bot_detection,
            authenticate_user_id=command.authenticate_user_id
        )

        return await self.repository.create(analytics)
