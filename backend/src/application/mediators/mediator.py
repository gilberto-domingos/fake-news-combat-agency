from src.application.query.get_animation_frames_query import GetAnimationFramesQuery
from src.application.query_handlers.get_animation_frames_query_handler import GetAnimationFramesQueryHandler


class Mediator:

    def __init__(self):
        self._handlers = {}

        # registro
        self._handlers[GetAnimationFramesQuery] = GetAnimationFramesQueryHandler()

    def register(self, command_type, handler):
        self._handlers[command_type] = handler

    async def send(self, command):
        command_type = type(command)

        handler = self._handlers.get(command_type)

        if not handler:
            raise ValueError(f"No handler registered for {command_type}")

        return await handler.handle(command)
