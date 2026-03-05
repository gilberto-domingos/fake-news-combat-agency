import re

class Email:
    __slots__ = ("_value",)

    def __init__(self, value: str):
        if not value:
            raise ValueError("Email não pode estar vazio")

        if not self._is_valid(value):
            raise ValueError("Endereço de email inválido")

        self._value = value.lower()

    @staticmethod
    def _is_valid(value: str) -> bool:
        return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", value))

    @property
    def value(self) -> str:
        return self._value

    def __str__(self):
        return self._value

    def __eq__(self, other):
        if not isinstance(other, Email):
            return False
        return self._value == other._value

    def __hash__(self):
        return hash(self._value)
