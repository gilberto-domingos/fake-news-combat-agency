from fastapi import Request
from fastapi import APIRouter, Depends, status

from src.api.dependencies import get_mediator
from src.application.mediator.mediator import Mediator

from src.application.command.analytics_access_crt_cmm import (
    AnalyticsAccessCreateCommand,
    RequestMetadata
)

from src.application.dto.analytics_access_res_dto import AnalyticsAccessResDto

router = APIRouter(
    prefix="/analytics_access",
    tags=["AnalyticsAccess"]
)


@router.post("/", response_model=AnalyticsAccessResDto, status_code=status.HTTP_201_CREATED)
async def create_analytics_access(
        payload: AnalyticsAccessCreateCommand,
        request: Request,
        mediator: Mediator = Depends(get_mediator)
):
    metadata = RequestMetadata(
        ip_address=request.client.host,
        country="BR",
        bot_detection=False
    )

    analytics = await mediator.send(payload, metadata)

    return AnalyticsAccessResDto.model_validate(
        analytics,
        from_attributes=True
    )
