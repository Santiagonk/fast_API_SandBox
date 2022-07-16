from typing import List
from fastapi import APIRouter, Depends, status
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.schemas import Login
from app.repository import auth

router = APIRouter(
    prefix="/login",
    tags=["Login"]
)

@router.post('/', status_code=status.HTTP_200_OK)
def login(user: Login, db: Session = Depends(get_db)):
    auth.auth_user(user, db)
    return {"res": "Login accepted"}