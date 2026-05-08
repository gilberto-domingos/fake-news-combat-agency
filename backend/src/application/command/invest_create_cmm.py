from dataclasses import dataclass


@dataclass(frozen=True)
class InvestCreateCommand:
    name: str
    proposal: str
    email: str
