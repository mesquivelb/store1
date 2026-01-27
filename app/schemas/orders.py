from pydantic import BaseModel
from typing import List

class OrderBase(BaseModel):
    user_id: int
    total: float | None = 0.0
    status: str | None = "pending"

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True