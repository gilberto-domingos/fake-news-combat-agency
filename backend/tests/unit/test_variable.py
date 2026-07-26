import pytest
from unittest.mock import AsyncMock

from src.module.digital_evidence.application.monitoring_orchestration.monitoring_worker import MonitoringWorker


@pytest.mark.asyncio
async def test_verify_value_monitoring_worker_keywords():
    repository = AsyncMock()
    search_content_service = AsyncMock()

    # # Simulating the repository return with two arrays
    repository.find_active_keywords.return_value = (
        ["python", "fastapi"],
        ["Laranja", "Banana"],
    )

    worker = MonitoringWorker(
        repository=repository,
        search_content_service=search_content_service,
    )

    await worker.execute([], [])

    received_value = (
        search_content_service.forward_search_engines
        .call_args.kwargs["monitoring_worker_keywords"]
    )

    print("Valuel of monitoring_worker_keywords:", received_value)
