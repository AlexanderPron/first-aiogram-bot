from utils.constants import *
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from core.handlers.base import (
    command_start_handler,
    select_master,
    master_room,
    start_handler,
    process_simple_calendar,
    master_calendar,
)
from core.commands import set_commands
from utils.DBot import DBot
from aiogram import F
from utils.aiogram3_calendar.simple_calendar import SimpleCalendarCallback as simple_cal_callback


async def start_bot(bot: Bot):
    logger.warning('Bot started')
    await set_commands(bot)


def stop_bot():
    logger.warning('Bot stoped')


async def main() -> None:
    dp = Dispatcher()
    bot = Bot(API_TOKEN, parse_mode="HTML")
    dbot = DBot(engine_str)
    dbot.create_db()

    dp.startup.register(start_bot)
    dp.message.register(command_start_handler, Command('start'))
    dp.callback_query.register(select_master, F.data.startswith('choose_master'))
    dp.callback_query.register(master_room, F.data.startswith('set_master'))
    dp.callback_query.register(start_handler, F.data == 'start_keyboard')
    dp.callback_query.register(process_simple_calendar, simple_cal_callback.filter())
    dp.callback_query.register(master_calendar, F.data.startswith('make_appointment::'))
    dp.shutdown.register(stop_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
