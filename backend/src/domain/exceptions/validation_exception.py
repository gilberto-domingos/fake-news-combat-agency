from domain.exceptions.domain_exception import DomainException

class ValidationException(DomainException):
    """ Exception for data validation errors.
        Example: invalid email, weak password, required field not filled. """
    pass