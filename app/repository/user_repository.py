
from telnetlib import SE
from sqlalchemy.orm import Session
from app.db import models
from app.schemas import UpdateUser

def create_user(user, db: Session):
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

def get_user_by_id(user_id, db:Session):
    user_response = db.query(models.User).filter(models.User.id == user_id).first()
    if not user_response:
        return {"message": "User Not Found"}
    return user_response

def delete_user(user_id, db: Session):
    user_response = db.query(models.User).filter(models.User.id == user_id)
    if not user_response.first():
        return {"message": "User Not Found"}
    user_response.delete(synchronize_session=False)
    db.commit()
    return {"message": "User deleted succesfully"}

def get_users(db: Session):
    user_response = db.query(models.User).all()
    return user_response

def update_user(user_id, db: Session, updateUser):
    user_response = db.query(models.User).filter(models.User.id == user_id)
    if not user_response.first():
        return {"message": "User Not Found"}
    user_response.update(updateUser.dict(exclude_unset=True))    
    db.commit()
    return {"message": "User updated succesfully"}
