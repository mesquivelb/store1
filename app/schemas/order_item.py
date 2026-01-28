from pydantic import BaseModel

class OrderItemBase(BaseModel):
    order_id: int
    product_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemCreate):
    id: int
    price: float

    class Config:
        orm_mode = True