from dataclasses import dataclass


@dataclass(frozen=True)
class AccessCounterCommand:
    access_counter: int
