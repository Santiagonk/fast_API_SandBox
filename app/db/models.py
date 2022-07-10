from datetime import datetime

from app.db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

"""
class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: Optional[str]
    phone_number: int
    created_at: datetime = datetime.now()


"""

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    phone_number = Column(Integer)
    email = Column(String)
    created_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    status = Column(Boolean)
