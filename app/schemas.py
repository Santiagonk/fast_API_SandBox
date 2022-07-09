# Python
from typing import Optional
from datetime import datetime

# pydantic
from pydantic import BaseModel

# User Model
class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: Optional[str]
    phone_number: int
    created_at: datetime = datetime.now()

class UserId(BaseModel):
    id:int
