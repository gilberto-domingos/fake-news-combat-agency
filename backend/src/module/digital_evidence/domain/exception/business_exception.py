from typing import Optional
from src.module.digital_evidence.domain.exception.domain_exception import DomainException


class BusinessException(DomainException):
    def __init__(
            self,
            message: str,
            error_code: Optional[str] = None
    ):
        super().__init__(
            message=message,
            error_code=error_code
        )
