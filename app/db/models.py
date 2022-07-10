from datetime import datetime

from app.db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    phone_number = Column(Integer)
    email = Column(String)
    created_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    status = Column(Boolean)
    sale = relationship("Sale", backref="user", cascade="delete,merge")

class Sale(Base):
    __tablename__ = "sale"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    sale = Column(Integer)
    sale_product = Column(Integer)