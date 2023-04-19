from utils.constants import *
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from core.handlers.base import (
    command_start_handler,
    echo_handler,
    start_bot,
    stop_bot,
)
from utils.DBot import DBot


async def main() -> None:
    dp = Dispatcher()
    bot = Bot(API_TOKEN, parse_mode="HTML")
    dbot = DBot(engine_str)
    dbot.create_db()

    dp.message.register(command_start_handler, Command(commands=["start"]))
    dp.message.register(echo_handler)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
