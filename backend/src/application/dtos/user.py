from pydantic import BaseModel

class CreateUserDTO(BaseModel):
    username: str
    email: str
    password: str

class UserResponseDTO(BaseModel):
    id: str
    username: str
    email: str
    created_at: str
