from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.command.user_create_cmm import CreateUserCommand
from src.application.command.analytics_access_crt_cmm import AnalyticsAccessCreateCommand
from src.application.command.invest_create_cmm import InvestCreateCommand

from src.application.command_handler.user_create_handler import CreateUserHandler
from src.application.command_handler.analytics_access_crt_handler import AnalyticsAccessCreateHandler
from src.application.command_handler.invest_create_handler import InvestCreateHandler
from src.application.query.analytics_access_query import AnalyticsAccessQuery
from src.application.query_handler.analytics_access_query_handler import AnalyticsAccessQueryHandler

from src.application.service.user_service import UserService

from src.domain.repository_int.user import PasswordHasher, UserRepository

from src.infrastructure.repository_impl.user import UserRepositoryImpl, BcryptPasswordHasher
from src.infrastructure.repository_impl.invest import InvestRepositoryImpl
from src.infrastructure.repository_impl.analytics_access_rep_impl import AnalyticsAccessRepositoryImpl

from src.application.mediator.comm_mediator import CommandMediator
from src.application.mediator.query_mediator import QueryMediator

from src.infrastructure.database.connection import get_session_factory


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    session_factory = get_session_factory()
    async with session_factory() as session:
        yield session


def get_user_repository(
        session: AsyncSession = Depends(get_db_session)
) -> UserRepositoryImpl:
    return UserRepositoryImpl(session)


def get_invest_repository(
        session: AsyncSession = Depends(get_db_session)
) -> InvestRepositoryImpl:
    return InvestRepositoryImpl(session)


def get_analytics_access_repository(
        session: AsyncSession = Depends(get_db_session)
) -> AnalyticsAccessRepositoryImpl:
    return AnalyticsAccessRepositoryImpl(session)


def get_password_hasher() -> PasswordHasher:
    return BcryptPasswordHasher()


def get_create_user_service(
        repo: UserRepository = Depends(get_user_repository),
        password_hasher: PasswordHasher = Depends(get_password_hasher)
) -> UserService:
    return UserService(
        user_repository=repo,
        password_hasher=password_hasher
    )


def get_create_user_handler(
        user_service: UserService = Depends(get_create_user_service)
) -> CreateUserHandler:
    return CreateUserHandler(user_service=user_service)


def get_invest_create_handler(
        repository: InvestRepositoryImpl = Depends(get_invest_repository)
) -> InvestCreateHandler:
    return InvestCreateHandler(repository)


def get_analytics_access_create_handler(
        repository: AnalyticsAccessRepositoryImpl = Depends(get_analytics_access_repository)
) -> AnalyticsAccessCreateHandler:
    return AnalyticsAccessCreateHandler(repository)


def get_analytics_access_query_handler(
        repository: AnalyticsAccessRepositoryImpl = Depends(get_analytics_access_repository)
) -> AnalyticsAccessQueryHandler:
    return AnalyticsAccessQueryHandler(repository)


def get_command_mediator(
        create_user_handler: CreateUserHandler = Depends(get_create_user_handler),
        invest_create_handler: InvestCreateHandler = Depends(get_invest_create_handler),
        analytics_access_crt_handler: AnalyticsAccessCreateHandler = Depends(get_analytics_access_create_handler),
) -> CommandMediator:
    comm_mediator = CommandMediator()

    comm_mediator.register(CreateUserCommand, create_user_handler)
    comm_mediator.register(InvestCreateCommand, invest_create_handler)
    comm_mediator.register(AnalyticsAccessCreateCommand, analytics_access_crt_handler)

    return comm_mediator


def get_query_mediator(
        analytics_access_query_handler: AnalyticsAccessQueryHandler = Depends(get_analytics_access_query_handler)
) -> QueryMediator:
    query_mediator = QueryMediator()

    query_mediator.register(AnalyticsAccessQuery, analytics_access_query_handler)

    return query_mediator
