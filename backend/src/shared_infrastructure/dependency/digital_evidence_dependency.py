from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.shared_infrastructure.database.connection import get_session_factory

from src.module.digital_evidence.application.mediator.comm_mediator import CommandMediator

# Commands
from src.module.digital_evidence.application.command.evidence_create_cmd import EvidenceCreateCommand
from src.module.digital_evidence.application.command.evidence_snapshot_create_cmd import EvidenceSnapshotCreateCommand
from src.module.digital_evidence.application.command.monitoring_target_create_cmd import MonitoringTargetCreateCommand
from src.module.digital_evidence.application.command.incident_create_cmd import IncidentCreateCommand

# Handlers
from src.module.digital_evidence.application.command_handler.evidence_create_handler import (
    EvidenceCreateHandler,
)

from src.module.digital_evidence.application.command_handler.evidence_snapshot_create_handler import (
    EvidenceSnapshotCreateHandler,
)

from src.module.digital_evidence.application.command_handler.monitoring_target_create_handler import (
    MonitoringTargetCreateHandler,
)
from src.module.digital_evidence.application.command_handler.incident_create_handler import (
    IncidentCreateHandler,
)

# Services
from src.module.digital_evidence.application.service_use_case.evidence_create_service import (
    EvidenceCreateService,
)

from src.module.digital_evidence.application.service_use_case.evidence_snapshot_create_service import (
    EvidenceSnapshotCreateService,
)

from src.module.digital_evidence.application.service_use_case.monitoring_target_create_service import (
    MonitoringTargetCreateService,
)
from src.module.digital_evidence.application.service_use_case.incident_create_service import (
    IncidentCreateService,
)

# Repository Interfaces
from src.module.digital_evidence.domain.repository_interface.evidence_interface import (
    EvidenceInterface,
)

from src.module.digital_evidence.domain.repository_interface.evidence_snapshot_interface import (
    EvidenceSnapshotInterface,
)

from src.module.digital_evidence.domain.repository_interface.monitoring_target_interface import (
    MonitoringTargetInterface,
)
from src.module.digital_evidence.domain.repository_interface.incident_interface import (
    IncidentInterface,
)

# Repository Implementations
from src.module.digital_evidence.infrastructure.repository_implement.evidence_implement import (
    EvidenceImplement,
)

from src.module.digital_evidence.infrastructure.repository_implement.evidence_snapshot_implement import (
    EvidenceSnapshotImplement,
)

from src.module.digital_evidence.infrastructure.repository_implement.monitoring_target_implement import (
    MonitoringTargetImplement,
)
from src.module.digital_evidence.infrastructure.repository_implement.incident_implement import (
    IncidentImplement,
)


# =====================================================================
# SESSION
# =====================================================================

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    session_factory = get_session_factory()

    async with session_factory() as session:
        yield session


# =====================================================================
# REPOSITORIES
# =====================================================================

def get_evidence_repository(
        session: AsyncSession = Depends(get_db_session),
) -> EvidenceInterface:
    return EvidenceImplement(session)


def get_evidence_snapshot_repository(
        session: AsyncSession = Depends(get_db_session),
) -> EvidenceSnapshotInterface:
    return EvidenceSnapshotImplement(session)


def get_monitoring_target_repository(
        session: AsyncSession = Depends(get_db_session),
) -> MonitoringTargetInterface:
    return MonitoringTargetImplement(session)


def get_incident_repository(
        session: AsyncSession = Depends(get_db_session),
) -> IncidentInterface:
    return IncidentImplement(session)


# =====================================================================
# SERVICES
# =====================================================================

def get_evidence_create_service(
        evidence_repository: EvidenceInterface = Depends(
            get_evidence_repository
        ),
        incident_repository: IncidentInterface = Depends(
            get_incident_repository
        ),
) -> EvidenceCreateService:
    return EvidenceCreateService(
        evidence_repository,
        incident_repository
    )


def get_evidence_snapshot_create_service(
        evidence_snapshot_repository: EvidenceSnapshotInterface = Depends(
            get_evidence_snapshot_repository
        ),
        evidence_repository: EvidenceInterface = Depends(
            get_evidence_repository
        ),
) -> EvidenceSnapshotCreateService:
    return EvidenceSnapshotCreateService(
        evidence_snapshot_repository,
        evidence_repository
    )


def get_monitoring_target_create_service(
        monitoring_target_repository: MonitoringTargetInterface = Depends(
            get_monitoring_target_repository
        ),
) -> MonitoringTargetCreateService:
    return MonitoringTargetCreateService(
        monitoring_target_repository
    )


def get_incident_create_service(
        incident_repository: IncidentInterface = Depends(
            get_incident_repository
        ),
        monitoring_target_repository: MonitoringTargetInterface = Depends(
            get_monitoring_target_repository
        ),
) -> IncidentCreateService:
    return IncidentCreateService(
        incident_repository,
        monitoring_target_repository
    )


# =====================================================================
# HANDLERS
# =====================================================================

def get_create_evidence_handler(
        evidence_service: EvidenceCreateService = Depends(
            get_evidence_create_service
        ),
) -> EvidenceCreateHandler:
    return EvidenceCreateHandler(
        evidence_service
    )


def get_create_evidence_snapshot_handler(
        evidence_snapshot_service: EvidenceSnapshotCreateService = Depends(
            get_evidence_snapshot_create_service
        ),
) -> EvidenceSnapshotCreateHandler:
    return EvidenceSnapshotCreateHandler(
        evidence_snapshot_service
    )


def get_create_monitoring_target_handler(
        monitoring_target_service: MonitoringTargetCreateService = Depends(
            get_monitoring_target_create_service
        ),
) -> MonitoringTargetCreateHandler:
    return MonitoringTargetCreateHandler(
        monitoring_target_service
    )


def get_create_incident_handler(
        incident_service: IncidentCreateService = Depends(
            get_incident_create_service
        ),
) -> IncidentCreateHandler:
    return IncidentCreateHandler(
        incident_service
    )


# =====================================================================
# MEDIATOR
# =====================================================================

def get_command_mediator(
        create_evidence_handler: EvidenceCreateHandler = Depends(
            get_create_evidence_handler
        ),
        create_evidence_snapshot_handler: EvidenceSnapshotCreateHandler = Depends(
            get_create_evidence_snapshot_handler
        ),
        create_monitoring_target_handler: MonitoringTargetCreateHandler = Depends(
            get_create_monitoring_target_handler
        ),
        create_incident_handler: IncidentCreateHandler = Depends(
            get_create_incident_handler
        ),
) -> CommandMediator:
    mediator = CommandMediator()

    mediator.register(
        EvidenceCreateCommand,
        create_evidence_handler,
    )

    mediator.register(
        EvidenceSnapshotCreateCommand,
        create_evidence_snapshot_handler,
    )

    mediator.register(
        MonitoringTargetCreateCommand,
        create_monitoring_target_handler,
    )

    mediator.register(
        IncidentCreateCommand,
        create_incident_handler,
    )

    return mediator
