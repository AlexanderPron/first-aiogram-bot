from aiogram.utils.keyboard import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardBuilder,
)
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from utils.botObjects import MasterData

# def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
#     """
#     Создаёт реплай-клавиатуру с кнопками в один ряд
#     :param items: список текстов для кнопок
#     :return: объект реплай-клавиатуры
#     """
#     row = [KeyboardButton(text=item) for item in items]
#     return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)


def start_keyboard() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.button(text='Информация', callback_data='get_info')
    kb_builder.button(text='Выбор мастера', callback_data='choose_master')
    kb_builder.button(text='Редактировать запись', callback_data='edit_record')
    kb_builder.adjust(2)
    return kb_builder.as_markup()


def choose_master_keyboard(masters: list[MasterData]) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    if len(masters) > 0:
        for master in masters:
            kb_builder.button(
                text=f'{master.first_name} {master.last_name}',
                callback_data=f'set_master::{master.master_id}',
            )
        kb_builder.adjust(3)
    else:
        pass
    return kb_builder.as_markup()


def selected_master_keyboard(master: MasterData) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.button(
        text='О мастере',
        callback_data=f'master_info::{master.master_id}',
    )
    kb_builder.button(
        text='График работы',
        callback_data=f'master_schedule::{master.master_id}',
    )
    kb_builder.button(
        text='Записаться',
        callback_data=f'make_appointment::{master.master_id}',
    )
    kb_builder.adjust(2)
    return kb_builder.as_markup()
