from typing import Dict, Type, Any


class QueryMediator:
    def __init__(self):
        self._handlers: Dict[Type, Any] = {}

    def register(self, query_type: Type, handler: Any) -> None:
        self._handlers[query_type] = handler

    async def send(self, query) -> Any:
        query_type = type(query)

        handler = self._handlers.get(query_type)

        if not handler:
            raise ValueError(
                f"No handler registered for query {query_type}"
            )

        return await handler.handle(query)
