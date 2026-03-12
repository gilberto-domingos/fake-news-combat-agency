from pydantic import BaseModel


class AccessCounterDto(BaseModel):
    access_counter: int
