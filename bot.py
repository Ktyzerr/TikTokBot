from aiogram import Bot, Dispatcher, F, Router, BaseMiddleware
from handlers import start
from aiogram.fsm.storage.memory import MemoryStorage
from middleware.IsMember import IsMember
import asyncio

GROUP_ID = 1234567890

async def main():
    bot = Bot('7543055577:AAF1NsrulpPHd1faFAB_qgqogMKn8t9qfOQ')
    dp = Dispatcher(storage=MemoryStorage())

    dp.message.middleware(IsMember(group_id=GROUP_ID))
    dp.callback_query.middleware(IsMember(group_id=GROUP_ID))
    dp.update.outer_middleware(IsMember(group_id=GROUP_ID))  

    dp.include_routers(start.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
