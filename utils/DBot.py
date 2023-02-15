'''Работа с бд'''

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import (
    MultipleResultsFound,
    NoResultFound,
)
from utils.DBotModels import Users
from utils.botObjects import UserData
from utils.constants import Base


class DBot(object):
    """Класс для работы с БД"""

    def __init__(self, engine_str):
        self.engine = create_engine(engine_str)
        self.session = Session(bind=self.engine)

    def create_db(self) -> bool:
        try:
            md = Base.metadata
            md.create_all(self.engine)
            return True
        except Exception:  # TODO Расписать исключения
            return False

    def add_user(self, user: UserData) -> Users:
        new_user = Users(
            tg_user_id=user.tg_user_id,
            name=user.name,
            lastname=user.lastname,
            tg_username=user.tg_username,
            tg_chat_id=user.tg_chat_id,
        )
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user

    def get_user(self, tg_username=None, tg_user_id=None) -> Users:
        if tg_username:
            try:
                user = self.session.query(Users).filter(Users.tg_username == tg_username).first()
            except MultipleResultsFound:
                return False
            except NoResultFound:
                return False
        if tg_user_id:
            try:
                user = self.session.query(Users).filter(Users.tg_user_id == tg_user_id).first()
            except MultipleResultsFound:
                return False
            except NoResultFound:
                return False
        return user
