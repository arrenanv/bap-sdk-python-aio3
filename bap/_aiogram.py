from typing import Any, Dict, Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message

from bap import Bap


class BapMiddleware(BaseMiddleware):
    def __init__(self, api_key: str):
        self._bap = Bap(api_key)

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ):
        need_to_handle = await self._bap.handle_update(
            # Dump by alias to change "from_user" field to "from"
            # as BAP API doesn't support it
            event.model_dump(exclude_none=True, by_alias=True)
        )

        if need_to_handle:
            return await handler(event, data)
