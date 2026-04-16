from src.application.query.get_animation_frames_query import GetAnimationFramesQuery
from src.application.dtos.animation.brick_dto import BrickDto
from src.application.dtos.animation.frame_dto import FrameDto
from src.application.dtos.animation.animation_response_dto import AnimationResponseDto


class GetAnimationFramesQueryHandler:

    async def handle(self, query: GetAnimationFramesQuery) -> AnimationResponseDto:
        frames_list = []

        for steps in range(query.steps):
            bricks_list = []
            for x in range(steps + 1):
                bricks_list.append(BrickDto(x=x, y=0))

            frames_list.append(FrameDto(bricks=bricks_list))

        return AnimationResponseDto(frames=frames_list)
