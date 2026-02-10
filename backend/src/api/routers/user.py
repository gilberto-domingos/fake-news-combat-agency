from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from application.dtos.user import CreateUserDTO, UserResponseDTO
from infrastructure.database.connection import get_session
from infrastructure.repositoriesImpl.user import UserRepositoryImpl
from application.commands.createUser import CreateUserCommand
from application.commandHandlers.createUserHandler import CreateUserHandler


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponseDTO, status_code=status.HTTP_201_CREATED)
async def create_user(payload: CreateUserDTO, session: AsyncSession = Depends(get_session)):
    repo = UserRepositoryImpl(session)
    handler = CreateUserHandler(repo)

    command = CreateUserCommand(
        username=payload.username,
        email=payload.email,
        password=payload.password
    )

    try:
        user = await handler.handle(command)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return UserResponseDTO(
        id=str(user.id),
        username=user.username,
        email=str(user.email),
        created_at=user.created_at.isoformat()
    )
