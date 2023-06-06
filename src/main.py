import requests
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional

from . import models, schemas
from .database import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Questions'
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


link = 'https://jservice.io/api/random?count=1'
counter = 0
error_message = 'Не удалось получить данные для вопроса'


def get_question():
    response = requests.get(link).json()
    if response:
        question_id = response[0]['id']
        question = response[0]['question']
        answer = response[0]['answer']
        return {'question_id': question_id, 'question': question, 'answer': answer}
    return None


def save_question_to_db(db, question_id, question, answer):
    new_question = models.Question(
        question_id=question_id,
        question=question,
        answer=answer
    )
    db.add(new_question)
    db.commit()
    db.refresh(new_question)


def question_exists(db, question_id):
    return db.query(models.Question).filter_by(question_id=question_id).first()


@app.post('/questions', response_model=Optional[schemas.QuestionResponse], tags=['Questions number'])
def create_questions(data: schemas.Question, db: Session = Depends(get_db)):
    global counter

    for _ in range(data.questions_num):
        response = get_question()
        if not response:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=error_message
            )
        question_id = response['question_id']
        if not question_exists(db, question_id):
            question = response['question']
            answer = response['answer']
            new_question = models.Question(
                question_id=question_id,
                question=question,
                answer=answer
            )
            save_question_to_db(db, question_id, question, answer)
            counter += 1
        else:
            while True:
                response = get_question()
                if not response:
                    raise HTTPException(
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail=error_message
                    )
                question_id = response['question_id']
                if not question_exists(db, question_id):
                    question = response['question']
                    answer = response['answer']
                    new_question = models.Question(
                        question_id=question_id,
                        question=question,
                        answer=answer
                    )
                    save_question_to_db(db, question_id, question, answer)
                    counter += 1
                    break
    if counter == 1:
        return None
    return db.query(models.Question).filter_by(id=counter-1).first()
