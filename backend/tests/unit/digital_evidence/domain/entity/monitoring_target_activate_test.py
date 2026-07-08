from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget
from uuid import UUID, uuid4
from faker import Faker

faker = Faker("pt_BR")


class MonitoringTargetTest:
    @staticmethod
    def run() -> None:
        variable = MonitoringTarget(
            id=uuid4(),
            target_name=faker.company(),
            is_active=False,
            keywords=["homicidio", "sequestro", "assalto"],
            created_at=faker.date_time()
        )
        print(f"Activate: {variable.is_active}")
        print(f"Keywords: {variable.keywords} ")

        try:
            variable.activate()
            print(f"Status after activate(): {variable.is_active}")

            variable.deactivate()
            print(f"Status after deactivate(): {variable.is_active}")


        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    MonitoringTargetTest.run()
