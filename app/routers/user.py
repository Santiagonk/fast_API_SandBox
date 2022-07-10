from typing import List
from fastapi import APIRouter, Depends
from app.schemas import UpdateUser, User, ShowUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.repository import user_repository

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.get('/', response_model=List[ShowUser])
def get_users(db: Session = Depends(get_db)):
    return user_repository.get_users(db)

@router.post('/signup')
def register_user(user_request: User, db: Session = Depends(get_db)):
    user_repository.create_user(user_request,db)
    return {"response": "User created succesfully"}

@router.get('/{user_id}', response_model=ShowUser)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user_response = user_repository.get_user_by_id(user_id, db)
    return user_response

@router.delete('/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_repository.delete_user(user_id, db)

@router.patch('/{user_id}')
def update_user(user_id: int, updateUser: UpdateUser, db: Session = Depends(get_db)):
    return user_repository.update_user(user_id, db, updateUser)
