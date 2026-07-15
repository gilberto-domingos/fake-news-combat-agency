# Rules and best practices for exception
# [Domain] -> throws business exception (BusinessException, ValidationException)
# [Application] -> can catch/rethrow or throw infrastructure exception
# [API] -> only catches exception and transforms them into HTTP/JSON (status 400/422/500)

from fastapi import FastAPI
from src.api.middleware.exception_handler import (
    business_exception_handler, validation_exception_handler, domain_exception_handler
)
from src.module.land.domain.exception.business_exception import BusinessException
from src.module.land.domain.exception.domain_exception import DomainException
from src.module.land.domain.exception.validation_exception import ValidationException
from src.api.exception_handler_http.global_exception_handler import global_exception_handler


def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(BusinessException, business_exception_handler)
    app.add_exception_handler(ValidationException, validation_exception_handler)
    app.add_exception_handler(DomainException, domain_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)
