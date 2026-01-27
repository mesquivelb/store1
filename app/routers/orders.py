from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.orders import Order, OrderCreate
from app.services.orders import create_order, get_order, list_orders
from app.database import get_db

router = APIRouter()
@router.post("/", response_model=Order)
def add_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, order)

@router.get("/", response_model=list[Order])
def all_orders(db: Session = Depends(get_db)):
    return list_orders(db)

@router.get("/{order_id}", response_model=Order)
def single_order(order_id: int, db: Session = Depends(get_db)):
    db_order = get_order(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
