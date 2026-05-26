# DomainException é a base de todas as exceções do domínio
class DomainException(Exception):
    """  Generic domain exception.
         All business rule, validation, or domain exception must inherit from it.  """

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
