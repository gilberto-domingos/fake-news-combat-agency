from pydantic import BaseModel

class CreateUserCommand(BaseModel):
    username: str
    email: str
    password: str
