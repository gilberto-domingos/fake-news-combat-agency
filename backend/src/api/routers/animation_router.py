from fastapi import APIRouter, Depends
from src.application.mediators.mediator import Mediator
from src.application.queries.get_sine_wave_motion_frames_query import GetSineWaveMotionFramesQuery

router = APIRouter(prefix="/animation", tags=["Animation"])


@router.get("/frames")
async def get_frames(mediator: Mediator = Depends()):
    query = GetSineWaveMotionFramesQuery(steps=120)
    return await mediator.send(query)
