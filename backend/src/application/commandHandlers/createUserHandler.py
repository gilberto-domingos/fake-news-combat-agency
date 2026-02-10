from domain.repositoriesCtr.user import UserRepository
from domain.entities.user import User
from domain.valueObjects.email import Email
from application.commands.createUser import CreateUserCommand

class CreateUserHandler:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def handle(self, command: CreateUserCommand) -> User:
        # verifica se já existe email
        existing_user = await self.user_repository.get_by_email(command.email)
        if existing_user:
            raise ValueError("Email already registered")

        # cria entidade
        user = User(
            username=command.username,
            email=Email(command.email),
            password=command.password
        )

        # persiste no banco
        await self.user_repository.save(user)
        return user
