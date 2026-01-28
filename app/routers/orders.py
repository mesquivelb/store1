from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.orders import OrderOut, OrderCreate
from app.services.orders import create_order, get_order, list_orders
from app.database import get_db
from app.auth.services import get_current_user_payload
from app.auth.schemas import UserPayload
from app.auth.services import require_admin



router = APIRouter()
@router.post("/", response_model=OrderOut)
def add_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, order)

@router.get("/", response_model=list[OrderOut])
def all_orders(db: Session = Depends(get_db), admin: UserPayload=Depends(require_admin)  ):
    return list_orders(db, admin.id )

@router.get("/{order_id}", response_model=OrderOut)
def single_order(order_id: int, db: Session = Depends(get_db), current_user:UserPayload=Depends(get_current_user_payload)):
    db_order = get_order(db, order_id, current_user.id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
