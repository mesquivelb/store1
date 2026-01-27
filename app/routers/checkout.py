from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.checkout import checkout_cart
from app.database import get_db

router = APIRouter()

@router.post("/user/{user_id}")
def checkout(user_id: int, db: Session = Depends(get_db)):
    order = checkout_cart(db, user_id)
    if not order:
        return {"message": "Cart is empty"}
    return {"order_id": order.id, "total": order.total}
