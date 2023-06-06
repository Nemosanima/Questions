from datetime import datetime

from pydantic import BaseModel, Field


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
