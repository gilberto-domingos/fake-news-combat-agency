from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.shared_infrastructure.database.connection import get_session_factory

from src.module.digital_evidence.application.mediator.comm_mediator import CommandMediator

# =====================================================================

from src.module.digital_evidence.application.command.evidence_create_cmd import (
    EvidenceCreateCommand,
)

from src.module.digital_evidence.application.command.evidence_snapshot_create_cmd import (
    EvidenceSnapshotCreateCommand,
)

from src.module.digital_evidence.application.command.monitoring_target_create_cmd import (
    MonitoringTargetCreateCommand,
)

from src.module.digital_evidence.application.command.incident_create_cmd import (
    IncidentCreateCommand,
)

# =====================================================================


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

# =====================================================================


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

# =====================================================================


from src.module.digital_evidence.domain.repository_interface.evidence_write_interface import (
    EvidenceInterface,
)

from src.module.digital_evidence.domain.repository_interface.evidence_snapshot_write_interface import (
    EvidenceSnapshotInterface,
)

from src.module.digital_evidence.domain.repository_interface.monitoring_target_write_interface import (
    MonitoringTargetInterface,
)

from src.module.digital_evidence.domain.repository_interface.incident_write_interface import (
    IncidentInterface,
)

# =====================================================================


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


# SESSION

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    session_factory = get_session_factory()

    async with session_factory() as session:
        yield session


# REPOSITORIES

def get_evidence_repository(
        session: AsyncSession = Depends(
            get_db_session
        ),
) -> EvidenceInterface:
    return EvidenceImplement(session)


def get_evidence_snapshot_repository(
        session: AsyncSession = Depends(
            get_db_session
        ),
) -> EvidenceSnapshotInterface:
    return EvidenceSnapshotImplement(session)


def get_monitoring_target_repository(
        session: AsyncSession = Depends(
            get_db_session
        ),
) -> MonitoringTargetInterface:
    return MonitoringTargetImplement(session)


def get_incident_repository(
        session: AsyncSession = Depends(
            get_db_session
        ),
) -> IncidentInterface:
    return IncidentImplement(session)


# SERVICES

def get_evidence_create_service(
        repository_evidence: EvidenceInterface = Depends(
            get_evidence_repository
        ),
        repository_incident: IncidentInterface = Depends(
            get_incident_repository
        ),
) -> EvidenceCreateService:
    return EvidenceCreateService(
        repository_evidence,
        repository_incident
    )


def get_evidence_snapshot_create_service(
        repository_snapshot: EvidenceSnapshotInterface = Depends(
            get_evidence_snapshot_repository
        ),
        repository_evidence: EvidenceInterface = Depends(
            get_evidence_repository
        ),
) -> EvidenceSnapshotCreateService:
    return EvidenceSnapshotCreateService(
        repository_snapshot,
        repository_evidence
    )


def get_monitoring_target_create_service(
        repository: MonitoringTargetInterface = Depends(
            get_monitoring_target_repository
        ),
) -> MonitoringTargetCreateService:
    return MonitoringTargetCreateService(
        repository
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


# HANDLERS

def get_evidence_create_handler(
        service: EvidenceCreateService = Depends(
            get_evidence_create_service
        ),
) -> EvidenceCreateHandler:
    return EvidenceCreateHandler(
        service
    )


def get_evidence_snapshot_create_handler(
        service: EvidenceSnapshotCreateService = Depends(
            get_evidence_snapshot_create_service
        ),
) -> EvidenceSnapshotCreateHandler:
    return EvidenceSnapshotCreateHandler(
        service
    )


def get_monitoring_target_create_handler(
        service: MonitoringTargetCreateService = Depends(
            get_monitoring_target_create_service
        ),
) -> MonitoringTargetCreateHandler:
    return MonitoringTargetCreateHandler(
        service
    )


def get_incident_create_handler(
        service: IncidentCreateService = Depends(
            get_incident_create_service
        ),
) -> IncidentCreateHandler:
    return IncidentCreateHandler(
        service
    )


# MEDIATOR

def get_command_mediator(
        evidence_create_handler: EvidenceCreateHandler = Depends(
            get_evidence_create_handler
        ),
        evidence_snapshot_create_handler: EvidenceSnapshotCreateHandler = Depends(
            get_evidence_snapshot_create_handler
        ),
        monitoring_target_create_handler: MonitoringTargetCreateHandler = Depends(
            get_monitoring_target_create_handler
        ),
        incident_create_handler: IncidentCreateHandler = Depends(
            get_incident_create_handler
        ),
) -> CommandMediator:
    mediator = CommandMediator()

    mediator.register(
        EvidenceCreateCommand,
        evidence_create_handler,
    )

    mediator.register(
        EvidenceSnapshotCreateCommand,
        evidence_snapshot_create_handler,
    )

    mediator.register(
        MonitoringTargetCreateCommand,
        monitoring_target_create_handler,
    )

    mediator.register(
        IncidentCreateCommand,
        incident_create_handler,
    )

    return mediator
