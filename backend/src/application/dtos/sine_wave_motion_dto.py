from pydantic import BaseModel


class SineWaveFrameDTO(BaseModel):
    x: float
    y: float
