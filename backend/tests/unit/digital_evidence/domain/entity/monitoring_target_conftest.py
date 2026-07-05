import pytest
from uuid import uuid4
from datetime import datetime

from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget


@pytest.fixture
def inactive_target():
    return MonitoringTarget(
        id=uuid4(),
        target_name="test",
        keywords=["python"],
        is_active=False,
        created_at=datetime.utcnow()
    )


@pytest.fixture
def active_target():
    return MonitoringTarget(
        id=uuid4(),
        target_name="test",
        keywords=["python"],
        is_active=True,
        created_at=datetime.utcnow()
    )


def test_should_activate_monitoring_target(inactive_target):
    inactive_target.activate()

    assert inactive_target.is_active is True


def test_should_raise_error_when_target_is_already_active(active_target):
    with pytest.raises(ValueError):
        active_target.activate()
