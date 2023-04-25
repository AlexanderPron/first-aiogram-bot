from aiogram.types import Message
from aiogram import types
from utils.constants import (
    logger,
    engine_str,
)
from utils.botObjects import UserData
from utils.DBot import DBot


async def command_start_handler(message: Message) -> None:
    new_user = UserData(
        tg_user_id=message.from_user.id,
        name=message.from_user.first_name,
        lastname=message.from_user.last_name,
        tg_username=message.from_user.username,
        tg_chat_id=message.chat.id,
    )
    dbot = DBot(engine_str)
    user = dbot.get_user(tg_user_id=message.from_user.id)
    if not user:
        user = dbot.add_user(new_user)  # TODO Добавить запись о добавлении пользователя в лог
    await message.answer(f"Hello, <b>{user.name} {user.lastname}</b>!\n\
Your username: <b>@{user.tg_username}</b>\n\
Your telegram id: <b>{user.tg_user_id}</b>")


async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        logger.debug("Not supported message type for copy")
        await message.answer("Not supported message type")
