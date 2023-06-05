from pydantic import BaseModel, Field


class Question(BaseModel):
    questions_num: int = Field(ge=1)
