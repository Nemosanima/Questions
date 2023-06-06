from pydantic import BaseModel, Field
from datetime import datetime


class Question(BaseModel):
    questions_num: int = Field(ge=1)


class QuestionResponse(BaseModel):
    id: int
    question_id: int
    question: str
    answer: str
    created: datetime

    class Config:
        orm_mode = True
