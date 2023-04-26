from aiogram.filters.callback_data import CallbackData


class MasterInfo(CallbackData, prefix='master'):
    name: str
    specialization: str
