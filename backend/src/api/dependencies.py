from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.command.access_counter_comm import AccessCounterCommand
from src.application.command.invest_create_cmm import InvestCreateCommand
from src.application.command_handlers.access_counter_handler import AccessCounterHandler
from src.application.command_handlers.invest_create_handler import InvestCreateHandler
from src.application.services.access_counter_service import AccessCounterService
from src.application.services.user_service import UserService
from src.infrastructure.database.connection import get_session_factory
from src.infrastructure.repositories_impl.user import UserRepositoryImpl, BcryptPasswordHasher
from src.infrastructure.repositories_impl.invest import InvestRepositoryImpl
from src.application.mediators.mediator import Mediator
from src.application.command.user_create_cmm import CreateUserCommand
from src.application.command_handlers.user_create_handler import CreateUserHandler
from src.domain.repositories_int.user import PasswordHasher, UserRepository


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


def get_password_hasher() -> PasswordHasher:
    return BcryptPasswordHasher()


def get_create_user_service(
        repo: UserRepository = Depends(get_user_repository),
        password_hasher=Depends(get_password_hasher)
) -> UserService:
    return UserService(user_repository=repo, password_hasher=password_hasher)


def get_create_user_handler(
        user_service: UserService = Depends(get_create_user_service)
) -> CreateUserHandler:
    return CreateUserHandler(user_service=user_service)


def get_invest_create_handler(
        repo: InvestRepositoryImpl = Depends(get_invest_repository)
) -> InvestCreateHandler:
    return InvestCreateHandler(repo)


def get_access_count_handler(
        access_counter_service: AccessCounterService = Depends()
) -> AccessCounterHandler:
    return AccessCounterHandler(access_counter_service)


def get_mediator(
        create_user_handler: CreateUserHandler = Depends(get_create_user_handler),
        access_counter_handler: AccessCounterHandler = Depends(get_access_count_handler),
        invest_create_handler: InvestCreateHandler = Depends(get_invest_create_handler)
) -> Mediator:
    mediator = Mediator()

    mediator.register(CreateUserCommand, create_user_handler)
    mediator.register(AccessCounterCommand, access_counter_handler)
    mediator.register(InvestCreateCommand, invest_create_handler)

    return mediator
