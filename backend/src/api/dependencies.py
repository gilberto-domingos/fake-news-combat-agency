from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.database.connection import get_session_factory
from src.infrastructure.repositories_impl.user import UserRepositoryImpl, BcryptPasswordHasher
from src.application.mediators.mediator import Mediator
from src.application.commands.create_user import CreateUserCommand
from src.application.command_handlers.create_user_handler import CreateUserHandler
from src.domain.repositories_int.user import PasswordHasher, UserRepository


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    session_factory = get_session_factory()

    async with session_factory() as session:
        yield session


def get_user_repository(
    session: AsyncSession = Depends(get_db_session)
) -> UserRepositoryImpl:
    return UserRepositoryImpl(session)

def get_password_hasher() -> PasswordHasher:
    return BcryptPasswordHasher()

def get_create_user_handler(
    repo: UserRepository = Depends(get_user_repository),
    password_hasher: PasswordHasher = Depends(get_password_hasher),
):
    return CreateUserHandler(repo, password_hasher)

def get_mediator(
    create_user_handler: CreateUserHandler = Depends(get_create_user_handler),
) -> Mediator:

    mediator = Mediator()

    mediator.register(CreateUserCommand, create_user_handler)

    return mediator