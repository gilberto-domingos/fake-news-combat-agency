import math
from typing import List
from src.application.dtos.sine_wave_motion_dto import SineWaveFrameDTO
from src.application.queries.get_sine_wave_motion_frames_query import GetSineWaveMotionFramesQuery


class GetSineWaveMotionFramesHandler:

    async def handle(self, query: GetSineWaveMotionFramesQuery) -> List[SineWaveFrameDTO]:
        frames = []

        for i in range(query.steps):
            x = i * 5
            y = 200 + 80 * math.sin(i * 0.1)

            frames.append(SineWaveFrameDTO(x=x, y=y))

        return frames
