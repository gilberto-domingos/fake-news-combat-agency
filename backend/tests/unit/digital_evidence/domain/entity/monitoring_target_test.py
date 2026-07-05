import pytest
from datetime import datetime
from uuid import UUID, uuid4
from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget


def test_should_deactivate_monitoring_target():
    # Arrange
    target = MonitoringTarget(
        id=uuid4(),
        target_name="Test",
        keywords=["Crime"],
        is_active=True,
        created_at=datetime.now()
    )

    # Action
    target.deactivate()

    # Assert
    assert target.is_active is False


def test_should_activate_monitoring_target():
    # Arrange
    target = MonitoringTarget(
        id=uuid4(),
        target_name="Test",
        keywords=["Crime"],
        is_active=False,
        created_at=datetime
    )

    # Action
    target.activate()

    # Assert
    assert target.is_active is True
