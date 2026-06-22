from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.module.land.infrastructure.database.connection import get_session_factory
from src.module.digital_evidence.infrastructure.repository_impl.digital_evidence_impl import DigitalEvidenceImpl


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    session_factory = get_session_factory()
    async with session_factory() as session:
        yield session


def get_evidence_repository(
        session: AsyncSession = Depends(get_db_session)
) -> DigitalEvidenceImpl:
    return DigitalEvidenceImpl(session)

# def get_user_repository(
#         session: AsyncSession = Depends(get_db_session)
# ) -> UserRepositoryImpl:
#     return UserRepositoryImpl(session)
