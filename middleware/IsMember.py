from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject, Message, CallbackQuery, User
from aiogram.exceptions import TelegramBadRequest


class IsMember(BaseMiddleware):
    def __init__(self, group_id: int):
        self.group_id = group_id

    async def is_user_in_group(self, bot: Bot, user_id: int) -> bool:
        try:
            member = await bot.get_chat_member(self.group_id, user_id)
            return member.status not in ["left", "kicked"]
        except TelegramBadRequest:
            return False

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        bot: Bot = data["bot"]

        user: User | None = data.get("event_from_user")
        if not user:
            return await handler(event, data)

        in_group = await self.is_user_in_group(bot, user.id)
        if not in_group:
            message: Message = data.get("message")
            callback: CallbackQuery = data.get("callback_query")

            if message:
                await message.answer("Please join our group: t.me/group_name")
            elif callback:
                await bot.send_message(user.id, "Please join our group: t.me/group_name")

            return

        return await handler(event, data)
