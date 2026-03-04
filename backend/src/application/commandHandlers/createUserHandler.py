from domain.exceptions.business_exception import BusinessException
from domain.repositoriesInt.user import UserRepository
from domain.entities.user import User
from domain.valueObjects.email import Email
from application.commands.createUser import CreateUserCommand
from uuid import UUID
from datetime import datetime


class CreateUserHandler:

    def __init__(self, user_repository: UserRepository, password_hasher):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    async def handle(self, command: CreateUserCommand) -> User:
        existing_user = await self.user_repository.get_by_email(command.email)
        if existing_user:
            raise BusinessException("Esse email já está registrado")

        password_hash = self.password_hasher.hash(command.password)

        user = User(
            name=command.name,
            lastname=command.lastname,
            email=Email(command.email),
            password_hash=password_hash,
            birthdate=command.birthdate,
            gender=command.gender,
            profession=command.profession,
            phone=command.phone,
        )
        await self.user_repository.save(user)
        return user

    def hash_password(self, password: str) -> str:
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()