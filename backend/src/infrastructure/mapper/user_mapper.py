from src.domain.entity.user import User
from src.domain.value_object.email import Email
from src.infrastructure.database.model.user_model import UserModel


class UserMapper:

    @staticmethod
    def to_model(user: User) -> UserModel:
        return UserModel(
            id=user.id,
            name=user.name,
            lastname=user.lastname,
            email=str(user.email),
            password_hash=user.password_hash,
            birthdate=user.birthdate,
            gender=user.gender,
            profession=user.profession,
            phone=user.phone
        )

    @staticmethod
    def to_entity(model: UserModel) -> User:
        return User(
            id=model.id,
            name=model.name,
            lastname=model.lastname,
            email=Email(model.email),
            password_hash=model.password_hash,
            birthdate=model.birthdate,
            gender=model.gender,
            profession=model.profession,
            phone=model.phone
        )
