from datetime import datetime

from app.db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    phone_number = Column(Integer)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    status = Column(Boolean, default=False)
    sale = relationship("Sale", backref="users", cascade="delete,merge")

class Sale(Base):
    __tablename__ = "sale"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    sale = Column(Integer)
    sale_product = Column(Integer)