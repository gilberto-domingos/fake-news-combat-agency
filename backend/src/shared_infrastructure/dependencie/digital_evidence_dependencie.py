from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.shared_infrastructure.database.connection import get_session_factory
from src.module.digital_evidence.application.mediator.comm_mediator import CommandMediator

from src.module.digital_evidence.infrastructure.repository_impl.digital_evidence_impl import DigitalEvidenceImpl
from src.module.digital_evidence.infrastructure.repository_impl.monitoring_target_impl import MonitoringTargetImpl

from src.module.digital_evidence.domain.repository_int.digital_evidence_rep_int import DigitalEvidenceRepositoryInt
from src.module.digital_evidence.domain.repository_int.monitoring_target_rep_int import MonitoringTargetRepInt

from src.module.digital_evidence.application.command_handler.digital_evidence_crt_handler import DigitalEvidenceHandler
from src.module.digital_evidence.application.command_handler.monitoring_target_crt_handler import \
    MonitoringTargetHandler

from src.module.digital_evidence.application.command.monitoring_target_crt_cmd import MonitoringTargetCrtCommand
from src.module.digital_evidence.application.command.digital_evidence_crt_comm import DigitalEvidenceCrtCommand


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    session_factory = get_session_factory()
    async with session_factory() as session:
        yield session


def get_digital_evidence_repository(
        session: AsyncSession = Depends(get_db_session)
) -> DigitalEvidenceRepositoryInt:
    return DigitalEvidenceImpl(session)


def get_monitoring_target_repository(
        session: AsyncSession = Depends(get_db_session)
) -> MonitoringTargetRepInt:
    return MonitoringTargetImpl(session)


def get_create_digital_evidence_handler(
        repository: DigitalEvidenceRepositoryInt = Depends(get_digital_evidence_repository)
) -> DigitalEvidenceHandler:
    return DigitalEvidenceHandler(repository)


def get_create_monitoring_target_handler(
        repository: MonitoringTargetRepInt = Depends(get_monitoring_target_repository)
) -> MonitoringTargetHandler:
    return MonitoringTargetHandler(repository)


def get_command_mediator(
        create_digital_evidence_handler: DigitalEvidenceHandler = Depends(get_create_digital_evidence_handler),
        create_monitoring_target_handler: MonitoringTargetHandler = Depends(get_create_monitoring_target_handler)
) -> CommandMediator:
    comm_mediator = CommandMediator()
    comm_mediator.register(DigitalEvidenceCrtCommand, create_digital_evidence_handler)
    comm_mediator.register(MonitoringTargetCrtCommand, create_monitoring_target_handler)

    return comm_mediator
