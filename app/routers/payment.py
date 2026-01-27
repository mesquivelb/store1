from fastapi import APIRouter
from app.services.payment import pay_order

router = APIRouter()

@router.post("/{order_id}")
def pay(order_id: int, amount: float):
    return pay_order(order_id, amount)