from src.application.queries.get_sine_wave_motion_frames_query import GetSineWaveMotionFramesQuery
from src.application.query_handlers.get_sine_wave_motion_frames_handler import GetSineWaveMotionFramesHandler


class Mediator:

    def __init__(self):
        self._handlers = {}

        # registro
        self._handlers[GetSineWaveMotionFramesQuery] = GetSineWaveMotionFramesHandler()

    def register(self, command_type, handler):
        self._handlers[command_type] = handler

    async def send(self, command):
        command_type = type(command)

        handler = self._handlers.get(command_type)

        if not handler:
            raise ValueError(f"No handler registered for {command_type}")

        return await handler.handle(command)

# class Mediator:
#
#     def __init__(self):
#         self._handlers = {}
#
#     def register(self, command_type, handler):
#         self._handlers[command_type] = handler
#
#     async def send(self, command):
#         command_type = type(command)
#
#         handler = self._handlers.get(command_type)
#
#         if not handler:
#             raise ValueError(f"No handler registered for {command_type}")
#
#         return await handler.handle(command)
