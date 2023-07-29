from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from ..db_setup import Base
from .mixins import Timestamp


class User(Timestamp, Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    orders = relationship("Order", back_populates="user")
    is_active = Column(Boolean, default=True)
