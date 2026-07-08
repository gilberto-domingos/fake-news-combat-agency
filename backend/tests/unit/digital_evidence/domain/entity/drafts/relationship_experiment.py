from uuid import uuid4
from faker import Faker

from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget
from src.module.digital_evidence.domain.entity.incident import Incident
from src.module.digital_evidence.domain.entity.evidence import Evidence
from src.module.digital_evidence.domain.entity.evidence_snapshot import EvidenceSnapshot
from src.module.digital_evidence.domain.enum.incident_status import IncidentStatus

faker = Faker("pt_BR")

status = faker.random_element(
    elements=[
        IncidentStatus.OPEN,
        IncidentStatus.CLOSED
    ]
)

target = MonitoringTarget(
    id=uuid4(),
    target_name=faker.company(),
    keywords=[
        faker.word(),
        faker.word(),
        faker.word()
    ],
    is_active=faker.boolean(),
    created_at=faker.date_time()
)

incident = Incident(
    id=uuid4(),
    title=faker.sentence(),
    monitoring_target=target,
    description=faker.text(),
    status=status,
    created_at=faker.date_time()
)

evidence = Evidence(
    id=uuid4(),
    incident=incident,
    url=faker.url(),
    source=faker.domain_name(),
    captured_at=faker.date_time(),
    hash=faker.sha256(),
    snapshots=[]
)

snapshot_1 = EvidenceSnapshot(
    id=uuid4(),
    evidence=evidence,
    screenshot_path=faker.file_path(depth=3, extension="png"),
    hash=faker.sha256(),
    text_content=faker.text(),
    html_path=faker.file_path(depth=3, extension="html")
)

snapshot_2 = EvidenceSnapshot(
    id=uuid4(),
    evidence=evidence,
    screenshot_path=faker.file_path(depth=3, extension="png"),
    hash=faker.sha256(),
    text_content=faker.text(),
    html_path=faker.file_path(depth=3, extension="html")
)

snapshot_3 = EvidenceSnapshot(
    id=uuid4(),
    evidence=evidence,
    screenshot_path=faker.file_path(depth=3, extension="png"),
    hash=faker.sha256(),
    text_content=faker.text(),
    html_path=faker.file_path(depth=3, extension="html")
)

snapshots = [
    snapshot_1,
    snapshot_2,
    snapshot_3
]

evidence.snapshots = snapshots

print(f"Dados do evidence: {evidence}")
