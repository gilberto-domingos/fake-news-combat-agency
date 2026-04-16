from pydantic import BaseModel


class BrickDto(BaseModel):
    x: int
    y: int
    type: str = "brick"
    intensity: float = 1.0
