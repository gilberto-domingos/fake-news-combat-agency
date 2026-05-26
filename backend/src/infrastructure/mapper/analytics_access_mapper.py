from src.domain.entity.analytics_access import AnalyticsAccess
from src.infrastructure.database.models.analytics_access_model import AnalyticsAccessModel


class AnalyticsAccessMapper:

    @staticmethod
    def to_model(analytics: AnalyticsAccess) -> AnalyticsAccessModel:
        return AnalyticsAccessModel(
            id=analytics.id,
            route=analytics.route,
            timestamp=analytics.timestamp,
            user_agent=analytics.user_agent,
            language=analytics.language,
            platform=analytics.platform,
            screen_width=analytics.screen_width,
            screen_height=analytics.screen_height,
            timezone=analytics.timezone,
            sessionId=analytics.sessionId,
            fingerprint=analytics.fingerprint,
            ip_address=analytics.ip_address,
            country=analytics.country,
            bot_detection=analytics.bot_detection,
            authenticate_user_id=analytics.authenticate_user_id
        )

    @staticmethod
    def to_entity(model: AnalyticsAccessModel) -> AnalyticsAccess:
        return AnalyticsAccess(
            id=model.id,
            route=model.route,
            timestamp=model.timestamp,
            user_agent=model.user_agent,
            language=model.language,
            platform=model.platform,
            screen_width=model.screen_width,
            screen_height=model.screen_height,
            timezone=model.timezone,
            sessionId=model.sessionId,
            fingerprint=model.fingerprint,
            ip_address=model.ip_address,
            country=model.country,
            bot_detection=model.bot_detection,
            authenticate_user_id=model.authenticate_user_id
        )
