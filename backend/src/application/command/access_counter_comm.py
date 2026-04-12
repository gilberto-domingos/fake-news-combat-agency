from dataclasses import dataclass


@dataclass(frozen=True)
class AccessCounterCommand:
    access_counter: int

class Test :
    def get_code(self):
