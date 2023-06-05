import requests
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='T1'
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/')
def create_questions(data: schemas.Question, db: Session = Depends(get_db)):
    return {'questions_num': data.questions_num}
