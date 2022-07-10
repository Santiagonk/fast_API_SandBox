from typing import List
from fastapi import APIRouter, Depends
from app.schemas import User, UserId, ShowUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.get('/', response_model=List[ShowUser])
def get_users(db: Session = Depends(get_db)):
    user_response = db.query(models.User).all()
    return user_response

@router.post('/signup')
def register_user(user: User, db: Session = Depends(get_db)):
    """
        username: str
        password: str
        first_name: str
        last_name: str
        address: Optional[str]
        phone_number: int
        email: str 
    """
    new_user = models.User(
        username = user.username,
        password = user.password,
        first_name = user.first_name,
        last_name = user.last_name,
        phone_number = user.phone_number,
        address = user.address,
        email = user.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"response": "User created succesfully"}

@router.get('/{user_id}', response_model=ShowUser)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    # for user in users:
    #     print(user, type)
    #     if user['id'] == user_id:
    #         return user
    user_response = db.query(models.User).filter(models.User.id == user_id).first()
    if not user_response:
        return {"message": "User Not Found"}
    return user_response

@router.post('/')
def obtener_usuario2(user_id:UserId):
    for user in users:
        print(user, type)
        if user['id'] == user_id.id:
            return user
    return {"message": "User Not Found"}

@router.delete('/{user_id}')
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user['id'] == user_id:
            users.pop(index)
            return {"message": "User deleted succesfully"}
    return {"message": "User Not Found"}

@router.put('/{user_id}')
def update_user(user_id: int, updateUser: User):
    for index, user in enumerate(users):
        if user['id'] == user_id:
            users[index]["first_name"] = updateUser.first_name
            users[index]["last_name"] = updateUser.last_name
            users[index]["address"] = updateUser.address
            users[index]["phone_number"] = updateUser.phone_number
            return {"message": "User updated succesfully"}
    return {"message": "User Not Found"}