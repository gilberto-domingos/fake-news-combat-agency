from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.shared_infrastructure.database.connection import get_session_factory
from src.module.digital_evidence.infrastructure.repository_impl.digital_evidence_impl import DigitalEvidenceImpl
from src.module.digital_evidence.domain.repository_int.digital_evidence_rep_int import DigitalEvidenceRepositoryInt
from src.module.digital_evidence.application.command_handler.digital_evidence_crt_handler import DigitalEvidenceHandler
from src.module.digital_evidence.application.command.digital_evidence_crt_comm import DigitalEvidenceCrtCommand
from src.module.digital_evidence.application.mediator.comm_mediator import CommandMediator


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    session_factory = get_session_factory()
    async with session_factory() as session:
        yield session


def get_digital_evidence_repository(
        session: AsyncSession = Depends(get_db_session)
) -> DigitalEvidenceRepositoryInt:
    return DigitalEvidenceImpl(session)


def get_create_digital_evidence_handler(
        repository: DigitalEvidenceRepositoryInt = Depends(get_digital_evidence_repository)
) -> DigitalEvidenceHandler:
    return DigitalEvidenceHandler(repository)


def get_command_mediator(
        create_digital_evidence_handler: DigitalEvidenceHandler = Depends(get_create_digital_evidence_handler),
) -> CommandMediator:
    comm_mediator = CommandMediator()
    comm_mediator.register(DigitalEvidenceCrtCommand, create_digital_evidence_handler)
    return comm_mediator
