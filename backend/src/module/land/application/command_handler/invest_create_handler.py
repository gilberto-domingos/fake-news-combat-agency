from src.module.land.application.command.invest_create_cmm import InvestCreateCommand
from src.module.land.domain.entity.invest import Invest
from src.module.land.domain.repository_int.invest import InvestRepository
from src.module.land.domain.value_object.email import Email


class InvestCreateHandler:
    def __init__(self, invest_repository: InvestRepository):
        self._invest_repository = invest_repository

    async def handle(self, command: InvestCreateCommand) -> Invest:
        invest = Invest(
            name=command.name,
            proposal=command.proposal,
            email=Email(command.email)
        )
        await self._invest_repository.save(invest)
        return invest
