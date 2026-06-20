from dataclasses import dataclass


@dataclass(frozen=True)
class DigitalEvidenceCrtCommand:
    url: str
    source: str
