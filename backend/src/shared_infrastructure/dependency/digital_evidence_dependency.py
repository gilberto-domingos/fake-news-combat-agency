from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.shared_infrastructure.database.connection import get_session_factory

from src.module.digital_evidence.application.mediator.comm_mediator import CommandMediator

# Commands
from src.module.digital_evidence.application.command.evidence_create_cmd import EvidenceCreateCommand
from src.module.digital_evidence.application.command.monitoring_target_create_cmd import MonitoringTargetCrtCommand
from src.module.digital_evidence.application.command.incident_create_cmd import IncidentCrtCommand

# Handlers
from src.module.digital_evidence.application.command_handler.evidence_create_handler import (
    EvidenceCreateHandler,
)
from src.module.digital_evidence.application.command_handler.monitoring_target_create_handler import (
    MonitoringTargetCrtHandler,
)
from src.module.digital_evidence.application.command_handler.incident_create_handler import (
    IncidentCrtHandler,
)

# Services
from src.module.digital_evidence.application.service_use_case.evidence_create_service import (
    EvidenceCreateService,
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
        repository: EvidenceInterface = Depends(
            get_evidence_repository
        ),
) -> EvidenceCreateService:
    return EvidenceCreateService(repository)


def get_monitoring_target_create_service(
        repository: MonitoringTargetInterface = Depends(
            get_monitoring_target_repository
        ),
) -> MonitoringTargetCreateService:
    return MonitoringTargetCreateService(repository)


def get_incident_create_service(
        repository: IncidentInterface = Depends(
            get_incident_repository
        ),
) -> IncidentCreateService:
    return IncidentCreateService(repository)


# =====================================================================
# HANDLERS
# =====================================================================

def get_create_evidence_handler(
        service: EvidenceCreateService = Depends(
            get_evidence_create_service
        ),
) -> EvidenceCreateHandler:
    return EvidenceCreateHandler(service)


def get_create_monitoring_target_handler(
        service: MonitoringTargetCreateService = Depends(
            get_monitoring_target_create_service
        ),
) -> MonitoringTargetCrtHandler:
    return MonitoringTargetCrtHandler(service)


def get_create_incident_handler(
        service: IncidentCreateService = Depends(
            get_incident_create_service
        ),
) -> IncidentCrtHandler:
    return IncidentCrtHandler(service)


# =====================================================================
# MEDIATOR
# =====================================================================

def get_command_mediator(
        create_evidence_handler: EvidenceCreateHandler = Depends(
            get_create_evidence_handler
        ),
        create_monitoring_target_handler: MonitoringTargetCrtHandler = Depends(
            get_create_monitoring_target_handler
        ),
        create_incident_handler: IncidentCrtHandler = Depends(
            get_create_incident_handler
        ),
) -> CommandMediator:
    mediator = CommandMediator()

    mediator.register(
        EvidenceCreateCommand,
        create_evidence_handler,
    )

    mediator.register(
        MonitoringTargetCrtCommand,
        create_monitoring_target_handler,
    )

    mediator.register(
        IncidentCrtCommand,
        create_incident_handler,
    )

    return mediator
