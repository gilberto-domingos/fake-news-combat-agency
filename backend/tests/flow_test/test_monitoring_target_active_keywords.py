import pytest

from src.module.digital_evidence.application.query.monitoring_target_active_keywords_query import (
    MonitoringTargetActiveKeywordsQuery
)
from src.module.digital_evidence.application.query_handler.monitoring_target_active_keywords_query_handler import (
    MonitoringTargetActiveKeywordsQueryHandler
)
from src.module.digital_evidence.application.service_use_case.monitoring_target_find_active_keywords_service import (
    MonitoringTargetFindActiveKeywordsService
)
from src.module.digital_evidence.infrastructure.repository_implement.monitoring_target_implement import (
    MonitoringTargetImplement
)
from src.shared_infrastructure.database.connection import (
    create_engine,
    create_session_factory,
    get_session_factory,
)


@pytest.mark.asyncio
async def test_find_active_keywords():
    ######### Arrange
    engine = create_engine()
    create_session_factory(engine)
    session_factory = get_session_factory()

    # Repository Implement
    async with session_factory() as session:
        repository = MonitoringTargetImplement(
            session=session
        )
        # Service Use Case
        service = MonitoringTargetFindActiveKeywordsService(
            repository=repository
        )

        # Query Handler
        handler = MonitoringTargetActiveKeywordsQueryHandler(
            service=service
        )

        # Query sent
        query = MonitoringTargetActiveKeywordsQuery(
            keywords=[],
            is_active=True
        )
        ######### Action
        # Triggers the entire flow
        result = await handler.handle(query)

        print("\nACTIVE KEYWORD RESULTS:")

        for keywords in result:
            print(keywords)

        ######### Assert
        # Validation
        assert result is not None
        assert isinstance(result, list)
