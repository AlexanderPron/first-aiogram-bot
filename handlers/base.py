from aiogram.filters import Command
from aiogram.types import Message
from aiogram import types
from utils.constants import logger
from utils.botObjects import UserData
from utils.DBot import DBot
from utils.constants import engine_str


async def command_start_handler(message: Message) -> None:
    new_user = UserData(
        tg_user_id=message.from_user.id,
        name=message.from_user.first_name,
        lastname=message.from_user.last_name,
        tg_username=message.from_user.username,
        tg_chat_id=message.chat.id,
    )
    dbot = DBot(engine_str)
    await dbot.add_user(new_user)
    print("ok")
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")


async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        logger.debug("Not supported message type for copy")
        await message.answer("Not supported message type")
