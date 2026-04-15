import math
from typing import List
from src.application.dtos.sine_wave_motion_dto import SineWaveFrameDTO
from src.application.queries.get_sine_wave_motion_frames_query import GetSineWaveMotionFramesQuery


class GetSineWaveMotionFramesHandler:

    async def handle(self, query):
        frames = []

        for h in range(query.height):
            frame = []

            for y in range(h + 1):
                for x in range(query.width):
                    frame.append({"x": x, "y": y})

            frames.append(frame)

        return frames
