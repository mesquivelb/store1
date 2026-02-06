from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.payment import pay_order
from app.database import get_db
from app.auth.services import get_current_user_payload
from app.auth.schemas import UserPayload

router = APIRouter()

@router.post("/{order_id}")
async def pay(
    order_id: int,
    amount: float,
    db: Session = Depends(get_db), 
    current_user: UserPayload = Depends(get_current_user_payload)
):
    return pay_order(db, order_id, amount, current_user.id)