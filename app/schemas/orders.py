from pydantic import BaseModel
from typing import List

class OrderBase(BaseModel):
    user_id: int
    total: float | None = 0.0
    status: str | None = "pending"

class OrderCreate(BaseModel):
    user_id: int

class OrderOut(BaseModel):
    id: int
    user_id: int
    total: float
    status: str

    class Config:
        orm_mode = True

class OrderUpdate(BaseModel):
    status: str
