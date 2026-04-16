# Rules and best practices for exceptions
# [Domain] -> throws business exceptions (BusinessException, ValidationException)
# [Application] -> can catch/rethrow or throw infrastructure exceptions
# [API] -> only catches exceptions and transforms them into HTTP/JSON (status 400/422/500)

from fastapi import FastAPI
from src.api.middlewares.exception_handler import (
    business_exception_handler, validation_exception_handler, domain_exception_handler
)
from src.domain.exceptions.business_exception import BusinessException
from src.domain.exceptions.domain_exception import DomainException
from src.domain.exceptions.validation_exception import ValidationException
from src.api.exception_handlers.global_exception_handler import global_exception_handler


def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(BusinessException, business_exception_handler)
    app.add_exception_handler(ValidationException, validation_exception_handler)
    app.add_exception_handler(DomainException, domain_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)
