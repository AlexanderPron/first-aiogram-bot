from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram import Bot
from utils.constants import (
    logger,
    engine_str,
    masters,
)
from utils.botObjects import UserData, MasterData
from utils.DBot import DBot
from core.keyboards.kb import (
    start_keyboard,
    choose_master_keyboard,
    selected_master_keyboard,
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


async def select_master(call: CallbackQuery):
    await call.message.answer(
        # text='Выберите мастера'.ljust(55, ' '),
        text='Выберите мастера',
        reply_markup=choose_master_keyboard(masters),
        parse_mode='html',
    )
    await call.answer()


async def master_room(call: CallbackQuery):
    master_id = call.data.split('::')[-1]
    # Ищем мастера с id master_id в списке мастеров masters
    try:
        master = next(filter(lambda master: master.master_id == int(master_id), masters))
    except ValueError:
        logger.error(f'id={master_id} - не число')
    except Exception as e:
        logger.error(f'Какая-то ошибка\n{e}')
    await call.message.answer(
        text=f'{master.first_name} {master.last_name}',
        reply_markup=selected_master_keyboard(master),
        parse_mode='html',
    )
    await call.answer()
