from src.module.land.domain.value_object.email import Email
from src.module.land.domain.entity.invest import Invest
from src.module.land.infrastructure.database.model.invest_model import InvestModel


class InvestMapper:

    @staticmethod
    def to_model(invest: Invest) -> InvestModel:
        return InvestModel(
            id=invest.id,
            name=invest.name,
            proposal=invest.proposal,
            email=str(invest.email)
        )

    @staticmethod
    def to_entity(model: InvestModel) -> Invest:
        return Invest(
            id=model.id,
            name=model.name,
            proposal=model.proposal,
            email=Email(model.email)
        )
