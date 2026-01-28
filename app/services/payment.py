from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.orders import Order

def pay_order(db: Session, order_id: int, amount: float, user_id: int):
    order = db.query(Order).filter(Order.id == order_id, Order.user_id == user_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if order.status == "paid":
        raise HTTPException(status_code=400, detail="Order already paid")

    if amount != order.total:
        raise HTTPException(status_code=400, detail="Incorrect payment amount")

    order.status = "paid"
    db.commit()
    db.refresh(order)

    return {
        "order_id": order.id,
        "amount_paid": amount,
        "status": order.status
    }