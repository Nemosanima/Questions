from sqlalchemy import TIMESTAMP, Column, Integer, String
from sqlalchemy.sql import func

from .database import Base


class Question(Base):
    __tablename__ = 'questions'

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    question_id = Column(
        Integer,
        name='Идентификатор вопроса'
    )
    question = Column(
        String,
        name='Вопрос'
    )
    answer = Column(
        String,
        name='Ответ'
    )
    created = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.current_timestamp(),
        name='Дата создания'
    )
