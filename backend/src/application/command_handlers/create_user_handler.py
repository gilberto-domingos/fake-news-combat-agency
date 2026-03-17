from src.application.command.create_user_cmm import CreateUserCommand
from src.application.services.user_service import UserService
from src.domain.entities.user import User
from src.domain.exceptions.business_exception import BusinessException
from src.infrastructure.external_services.recaptcha_service import verify_recaptcha


class CreateUserHandler:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def handle(self, command: CreateUserCommand) -> User:
        is_human = await verify_recaptcha(command.captcha_token)
        if not is_human:
            raise BusinessException("reCAPTCHA inválido. Verifique se você não é um robô.")

        user = await self.user_service.create_user(
            name=command.name,
            lastname=command.lastname,
            email=command.email,
            birthdate=command.birthdate,
            gender=command.gender,
            profession=command.profession,
            phone=command.phone,
            password=command.password,
            terms_accepted=command.terms_accepted
        )
        return user
