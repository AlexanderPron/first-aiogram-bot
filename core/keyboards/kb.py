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
from utils.aiogram3_calendar.calendar_types import SimpleCalendarCallback


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
        kb_builder.row(
            InlineKeyboardButton(
                text='Назад',
                callback_data='start_keyboard',
            ),
        )
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
    kb_builder.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data='choose_master',
        ),
        InlineKeyboardButton(
            text='В начало',
            callback_data='start_keyboard',
        ),
    )
    return kb_builder.as_markup()
