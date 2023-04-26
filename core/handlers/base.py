from aiogram.types import Message
from aiogram import types
from utils.constants import (
    logger,
    engine_str,
)
from utils.botObjects import UserData, MasterData
from utils.DBot import DBot
from core.keyboards.kb import (
    start_keyboard,
    choose_master_keyboard,
)


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
        user = dbot.add_user(new_user)
        logger.warning(f'New user added: tg_user_id - {user.tg_user_id}, tg_username - @{user.tg_username}')
    await message.answer(
        text=f'Здравствуйте, <b>{user.name} {user.lastname}</b>!\n\
Your username: <b>@{user.tg_username}</b>\n\
Your telegram id: <b>{user.tg_user_id}</b>',
        reply_markup=start_keyboard(),
        parse_mode='html',
    )


async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        logger.debug("Not supported message type for copy")
        await message.answer("Not supported message type")


async def select_master(message: Message) -> None:
    masters = []
    master1 = MasterData(
        master_id=1,
        first_name='Иван',
        last_name='Сусанин'
    )
    masters.append(master1)
    try:
        await message.answer(
            text='Выберите мастера                     ',
            reply_markup=choose_master_keyboard(masters),
            parse_mode='html',
        )
    except TypeError:
        logger.debug("Not supported message type for copy")
        await message.answer("Not supported message type")
