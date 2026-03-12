from src.application.services.access_counter_service import AccessCounterService
from src.application.command.access_counter_comm import AccessCounterCommand


class AccessCounterHandler:
    def __init__(self, access_counter_service: AccessCounterService):
        self.access_counter_service = access_counter_service

    async def handle(self, command: AccessCounterCommand):
        result = self.access_counter_service.calculate_accesses(command.access_counter)
        return result
