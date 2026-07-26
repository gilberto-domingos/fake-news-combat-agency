import pytest
from unittest.mock import AsyncMock

from src.module.digital_evidence.application.monitoring_orchestration.monitoring_worker import (
    MonitoringWorker
)

from src.module.digital_evidence.application.service_use_case.search_content_service import (
    SearchContentService
)

from src.module.digital_evidence.domain.repository_interface.monitoring_target_read_interface import (
    MonitoringTargetReadInterface
)

from src.module.digital_evidence.domain.repository_interface.search_content_gateway_interface import (
    SearchContentGatewayInterface
)


@pytest.mark.asyncio
async def test_monitoring_worker_flow():
    # Mock 1 - Repository Interface
    repository = AsyncMock(
        spec=MonitoringTargetReadInterface
    )

    repository.find_active_keywords.return_value = [
        ["python", "fastapi"]
    ]

    # Mock 2 - Gateway Interface
    search_gateway = AsyncMock(
        spec=SearchContentGatewayInterface
    )

    search_gateway.search_content_social_media.return_value = [
        ["result"]
    ]

    # Class
    search_content_service = SearchContentService(
        search_content_gateway_interface=search_gateway
    )

    # Class
    worker = MonitoringWorker(
        repository=repository,
        search_content_service=search_content_service
    )

    # Run flow
    result = await worker.execute(
        keywords=[],
        is_active=True
    )

    # View stream
    print("Value coming from Repository:")
    print(repository.find_active_keywords.return_value)

    print("Value arriving at Gateway:")
    print(
        search_gateway.search_content_social_media.call_args
    )

    print("Final result:")
    print(result)

    # Validate the passage of variables

    repository.find_active_keywords.assert_called_once_with(
        keywords=[],
        is_active=True
    )

    search_gateway.search_content_social_media.assert_called_once_with(
        keywords=[
            ["python", "fastapi"]
        ]
    )

    assert result == [
        ["result"]
    ]
