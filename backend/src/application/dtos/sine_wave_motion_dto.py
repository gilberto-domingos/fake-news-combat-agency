from pydantic import BaseModel


class SineWaveFrameDTO(BaseModel):
    x: int
    y: int
    type: str = "brick"
    intensity: float = 1.0
