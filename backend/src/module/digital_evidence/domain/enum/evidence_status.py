from enum import Enum


class EvidenceStatus(Enum):
    CAPTURED = "captured"
    PROCESSING = "processing"
    VALIDATED = "validated"
    FAILED = "failed"
