from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.order_item import OrderItem, OrderItemCreate
from app.services.order_item import create_order_item, list_order_items
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=OrderItem)
async def add_order_item(item: OrderItemCreate, db: Session = Depends(get_db)):
    return create_order_item(db, item)

@router.get("/order/{order_id}", response_model=list[OrderItem])
async def order_items(order_id: int, db: Session = Depends(get_db)):
    return list_order_items(db, order_id)
