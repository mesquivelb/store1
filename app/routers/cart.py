from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.cart import CartItem, CartItemCreate
from app.services.cart import add_to_cart, list_cart, clear_cart
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=CartItem)
def add_item(item: CartItemCreate, db: Session = Depends(get_db)):
    return add_to_cart(db, item)

@router.get("/user/{user_id}", response_model=list[CartItem])
def get_cart(user_id: int, db: Session = Depends(get_db)):
    return list_cart(db, user_id)

@router.delete("/user/{user_id}")
def empty_cart(user_id: int, db: Session = Depends(get_db)):
    clear_cart(db, user_id)
    return {"message": "Cart cleared"}
