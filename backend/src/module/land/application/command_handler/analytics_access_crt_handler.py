from src.module.land.application.command.analytics_access_crt_cmm import AnalyticsAccessCreateCommand, RequestMetadata
from src.module.land.domain.entity.analytics_access import AnalyticsAccess
from src.module.land.domain.repository_int.analytics_access_rep_int import AnalyticsAccessRepositoryInt
from src.module.land.domain.repository_int.geo_location_int import GeoLocationServiceInt
from uuid import uuid4


class AnalyticsAccessCreateHandler:
    def __init__(self, analytics_access_repository: AnalyticsAccessRepositoryInt,
                 geo_location_service: GeoLocationServiceInt):
        self.repository = analytics_access_repository
        self.geo_location_service = geo_location_service

    async def handle(self, command: AnalyticsAccessCreateCommand,
                     metadata: RequestMetadata | None = None):
        city = None

        if metadata:
            city = self.geo_location_service.get_city(
                metadata.ip_address
            )

        analytics = AnalyticsAccess(
            id=uuid4(),
            route=command.route,
            timestamp=command.timestamp,
            city=city,
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
