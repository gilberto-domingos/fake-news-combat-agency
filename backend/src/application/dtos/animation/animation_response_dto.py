from pydantic import BaseModel
from typing import List
from src.application.dtos.animation.frame_dto import FrameDto


class AnimationResponseDto(BaseModel):
    frames: List[FrameDto]
