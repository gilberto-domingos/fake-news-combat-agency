from fastapi import Request
from starlette.responses import JSONResponse
from src.module.land.domain.exception.business_exception import BusinessException
from src.module.land.domain.exception.validation_exception import ValidationException
from src.module.land.domain.exception.domain_exception import DomainException


async def business_exception_handler(
        request: Request,
        exc: BusinessException
) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"detail": exc.message}
    )


async def validation_exception_handler(
        request: Request,
        exc: ValidationException
) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content={"detail": exc.message}
    )


async def domain_exception_handler(
        request: Request,
        exc: DomainException
) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"detail": exc.message}
    )
