from src.module.digital_evidence.domain.entity.monitoring_target import MonitoringTarget
from src.module.digital_evidence.infrastructure.model.monitoring_target_model import MonitoringTargetModel


class MonitoringTargetMapper:

    @staticmethod
    def to_model(monitoring_target: MonitoringTarget) -> MonitoringTargetModel:
        return MonitoringTargetModel(
            id=monitoring_target.id,
            target_name=monitoring_target.target_name,
            keywords=monitoring_target.keywords,
            is_active=monitoring_target.is_active,
            created_at=monitoring_target.created_at
        )

    @staticmethod
    def to_entity(model: MonitoringTargetModel) -> MonitoringTarget:
        return MonitoringTarget(
            id=model.id,
            target_name=model.target_name,
            keywords=model.keywords,
            is_active=model.is_active,
            created_at=model.created_at
        )
