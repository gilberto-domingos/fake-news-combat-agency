from pydantic import BaseModel
from typing import List
from src.application.dtos.animation.brick_dto import BrickDto


class FrameDto(BaseModel):
    bricks: List[BrickDto]
