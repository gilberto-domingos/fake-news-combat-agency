from src.application.dtos.sine_wave_motion_dto import SineWaveFrameDTO
from src.application.queries.get_sine_wave_motion_frames_query import GetSineWaveMotionFramesQuery


class GetSineWaveMotionFramesHandler:

    async def handle(self, query):
        frames = []

        # 1. gera lista linear de “tijolos”
        bricks = []

        for i in range(query.width):
            bricks.append(
                SineWaveFrameDTO(
                    y=i // 10,
                    x=i % 10,
                    type="brick",
                    intensity=1.0
                ).model_dump()
            )

        # 2. constrói frames progressivos
        for i in range(len(bricks)):
            frame = bricks[:i + 1]
            frames.append(frame)

        return frames
