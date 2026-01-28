from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.cart import CartItem, CartItemCreate
from app.services.cart import add_to_cart, list_cart, clear_cart
from app.database import get_db
from app.auth.services import get_current_user_payload
from app.auth.schemas import UserPayload

router = APIRouter()

@router.post("/", response_model=CartItem)
def add_item(item: CartItemCreate, db: Session = Depends(get_db), current_user:UserPayload=Depends(get_current_user_payload) ):
    return add_to_cart(db, item, current_user.id)

@router.get("/", response_model=list[CartItem])
def get_cart( db: Session = Depends(get_db), current_user:UserPayload=Depends(get_current_user_payload)):
    return list_cart(db, current_user.id)

@router.delete("/", status_code=204)
def empty_cart(db: Session = Depends(get_db), current_user:UserPayload=Depends(get_current_user_payload)):
    clear_cart(db, current_user.id)
    return {"message": "Cart cleared"}
