from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Enum
from sqlalchemy.orm import relationship

from ..db_setup import Base
import enum

from .mixins import Timestamp


class PaymentStatus(enum.Enum):
    pending = 1
    completed = 2
    failed = 3


class Order(Timestamp, Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="orders")
    total_amount = Column(Float)
    payment_status = Column(Enum(PaymentStatus), default="pending")
    shipping_address = Column(String)
