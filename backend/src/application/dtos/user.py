from pydantic import BaseModel, EmailStr

class CreateUserDTO(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponseDTO(BaseModel):
    id: str
    username: str
    email: str
    created_at: str
