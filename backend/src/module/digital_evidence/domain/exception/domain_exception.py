from typing import Optional


class DomainException(Exception):
    def __init__(
            self,
            message: str,
            error_code: Optional[str] = None
    ):
        self._message = message
        self._error_code = error_code

        super().__init__(message)

    @property
    def message(self) -> str:
        return self._message

    @property
    def error_code(self) -> Optional[str]:
        return self._error_code
