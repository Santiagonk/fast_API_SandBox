# Python
from typing import Optional
from datetime import datetime

# pydantic
from pydantic import BaseModel

# User Model
class User(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    address: Optional[str]
    phone_number: int
    email: str
    created_at: datetime = datetime.now()

class UpdateUser(BaseModel):
    username: str = None
    password: str = None
    first_name: str = None
    last_name: str = None
    address: str = None
    phone_number: int = None
    email: str = None

class UserId(BaseModel):
    id:int

class ShowUser(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str
