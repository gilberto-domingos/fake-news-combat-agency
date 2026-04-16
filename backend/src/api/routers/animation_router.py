from fastapi import APIRouter, Depends
from src.application.mediators.mediator import Mediator
from src.application.query.get_animation_frames_query import GetAnimationFramesQuery

router = APIRouter(prefix="/animation", tags=["Animation"])


@router.get("/frames")
async def get_frames(mediator: Mediator = Depends()):
    query = GetAnimationFramesQuery(
        steps=120,
        height=20,
        width=10,
    )
    return await mediator.send(query)
