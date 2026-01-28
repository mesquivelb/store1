from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base
from app.models.products import Product
from app.models.users import User
from typing import Optional

class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int] = mapped_column(default=1)

    # Relaciones
    user: Mapped[User] = relationship("User", back_populates="cart_items")
    product: Mapped[Product] = relationship("Product", back_populates="cart_items")
