from sqlalchemy.orm import Session
from app.db import models
from app.schemas import UpdateUser
from fastapi import HTTPException, status
from app.hashing import Hash

def auth_user(user_request, db: Session):
    user = db.query(models.User).filter(models.User.username == user_request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The User with the username {user_request.username} doesn't exist"
        )
    if not Hash.verify_password(user_request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Wrong password"
        )

