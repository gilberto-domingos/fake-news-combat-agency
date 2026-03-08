from fastapi import Request
from starlette.responses import JSONResponse
from src.domain.exceptions.business_exception import BusinessException
from src.domain.exceptions.validation_exception import ValidationException
from src.domain.exceptions.domain_exception import DomainException


async def business_exception_handler(request: Request, exc: BusinessException):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.message}
    )


async def validation_exception_handler(request: Request, exc: ValidationException):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.message}
    )


async def domain_exception_handler(request: Request, exc: DomainException):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.message}
    )