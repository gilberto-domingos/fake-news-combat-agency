from uuid import UUID, uuid4
from datetime import datetime
from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget


class MonitoringTester:
    @staticmethod
    def run() -> None:
        target = MonitoringTarget(
            id=uuid4(),
            target_name="Google News",
            keywords=["crime", "calunia", "difamação"],
            is_active=False,
            created_at=datetime.now()
        )
        print(f"Name: {target.target_name}")
        print(f"Initial status: {target.is_active}")
        print(f"Keywords now : {target.keywords}")
        try:
            target.activate()
            print(f"States after activate(): {target.is_active}")

            target.deactivate()
            print(f"States after deactivate(): {target.is_active}")

            target.add_keywords([
                "agressão",
                "desinformação",
                "discurso de odio"

            ])

            print(f"Keywords new 'list' now : {target.keywords}")


        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    MonitoringTester.run()
