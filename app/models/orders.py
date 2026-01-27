from sqlalchemy import Column, Integer,ForeignKey, String, Float, DateTime

from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    # Relaciones
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    total = Column(Float, default=0.0)
    currency = Column(String, default="MXN")
    status = Column(String, index=True, default="pending")

    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    user = relationship("User", back_populates="orders")
    items = relationship(
        "OrderItem",back_populates="order",cascade="all, delete-orphan")
