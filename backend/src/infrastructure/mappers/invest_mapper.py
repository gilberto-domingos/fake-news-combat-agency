from src.domain.value_objects.email import Email
from src.domain.entities.invest import Invest
from src.infrastructure.database.models.invest_model import InvestModel


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
