from datetime import date

from src.domain.entities.user import User
from src.domain.exceptions.business_exception import BusinessException
from src.domain.repositories_int.user import UserRepository
from src.domain.value_objects.email import Email
from passlib.hash import bcrypt


class UserService:
    def __init__(self, user_repository: UserRepository, password_hasher=bcrypt):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    async def create_user(self,
                          name: str,
                          lastname: str,
                          email: str,
                          birthdate: date,
                          gender: str,
                          profession: str,
                          phone: str,
                          password: str,
                          terms_accepted: bool
                          ) -> User:
        existing_user = await self.user_repository.get_by_email(email)
        if existing_user:
            raise BusinessException("Email already registered")

        password_hash = self.password_hasher.hash(password)

        user = User(
            name=name,
            lastname=lastname,
            email=Email(email),
            birthdate=birthdate,
            gender=gender,
            profession=profession,
            phone=phone,
            password_hash=password_hash,
            terms_accepted=terms_accepted
        )
        await self.user_repository.save(user)
        return user
