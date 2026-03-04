from domain.exceptions.domain_exception import DomainException

class BusinessException(DomainException):
    """ Specific exception for business rules.
        Example: email already registered, balance limit exceeded, inactive user. """
    pass