from sqlalchemy.orm import Session
from app.models.orders import Order
from app.schemas.orders import OrderCreate

def create_order(db: Session, order_data: dict):
    db_order = Order(**order_data)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def list_orders(db: Session):
    return db.query(Order).all()
