from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    String,
    DateTime,
)
from utils.constants import Base
from datetime import datetime


class Users(Base):
    __tablename__ = "users"

    tg_user_id = Column(BigInteger, primary_key=True)
    name = Column(String(30), nullable=False)
    lastname = Column(String)
    tg_username = Column(String(30))
    tg_chat_id = Column(BigInteger)
    added_dt = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"User(id={self.tg_user_id}, name={self.name}, lastname={self.lastname})"
