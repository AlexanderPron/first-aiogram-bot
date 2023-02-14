from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserData:
    """Тип данных для пользователя"""
    tg_user_id: int = None
    name: str = None
    lastname: str = None
    tg_username: str = None
    tg_chat_id: str = None
    added_dt: datetime = None
