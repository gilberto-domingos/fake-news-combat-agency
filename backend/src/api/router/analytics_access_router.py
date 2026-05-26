from fastapi import Request
from fastapi import APIRouter, Depends, status

from src.api.dependencies import get_command_mediator
from src.api.dependencies import get_query_mediator

from src.application.mediator.comm_mediator import CommandMediator
from src.application.mediator.query_mediator import QueryMediator

from src.application.command.analytics_access_crt_cmm import (AnalyticsAccessCreateCommand, RequestMetadata)
from src.application.query.analytics_access_query import AnalyticsAccessQuery
from src.application.query.analytics_access_count_query import AnalyticsAccessCountQuery

from src.application.dto.analytics_access_res_dto import AnalyticsAccessResDto

router = APIRouter(
    prefix="/analytics_access",
    tags=["AnalyticsAccess"]
)


@router.post("/", response_model=AnalyticsAccessResDto, status_code=status.HTTP_201_CREATED)
async def create_analytics_access(
        payload: AnalyticsAccessCreateCommand,
        request: Request,
        mediator: CommandMediator = Depends(get_command_mediator)
):
    metadata = RequestMetadata(
        ip_address=request.client.host,
        country="BR",
        bot_detection=False
    )

    analytics = await mediator.send(payload, metadata)

    return AnalyticsAccessResDto.model_validate(analytics, from_attributes=True)


@router.get("/find_all", response_model=list[AnalyticsAccessResDto], status_code=status.HTTP_200_OK)
async def find_all(query: AnalyticsAccessQuery = Depends(),
                   query_mediator: QueryMediator = Depends(get_query_mediator)):
    analytics_list = await query_mediator.send(query)

    return [AnalyticsAccessResDto.model_validate(item, from_attributes=True) for item in analytics_list]


@router.get("/find_count", status_code=status.HTTP_200_OK)
async def find_count(
        query: AnalyticsAccessCountQuery = Depends(),
        query_mediator: QueryMediator = Depends(get_query_mediator)
):
    analytics_count = await query_mediator.send(query)

    return analytics_count
