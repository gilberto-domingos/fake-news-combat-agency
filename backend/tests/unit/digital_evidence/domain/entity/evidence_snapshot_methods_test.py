from uuid import uuid4
from faker import Faker
from src.module.digital_evidence.domain.entity.evidence_snapshot import EvidenceSnapshot

faker = Faker("pt_Br")


def test_should_generate_hash() -> None:
    # Arrange
    snapshot = EvidenceSnapshot(
        id=uuid4(),
        screenshot_path=faker.file_path(),
        hash=faker.sha256(),
        text_content=faker.text(),
        html_path=faker.file_path(depth=3, extension="html")
    )

    # Action
    result = snapshot.calculate_hash()

    # Assert
    assert isinstance(result, str)
    assert len(result) == 64
    print(f"Generated hash : {result}")


def test_should_verify_integrity_hash() -> None:
    # Arrange
    snapshot = EvidenceSnapshot(
        id=uuid4(),
        screenshot_path=faker.file_path(),
        hash=faker.sha256(),
        text_content=faker.text(),
        html_path=faker.file_path(depth=3, extension="html")
    )

    # Action
    snapshot.generate_hash()

    # Assert
    result = snapshot.validate_integrity() is True
    print(f"Hash Validation is: {result}")
