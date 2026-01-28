from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.checkout import checkout_cart
from app.database import get_db
from app.auth.services import get_current_user_payload
from app.auth.schemas import UserPayload


router = APIRouter()

@router.post("/")
def checkout( db: Session = Depends(get_db), current_user:UserPayload=Depends(get_current_user_payload)):
    order = checkout_cart(db, current_user.id)
    if not order:
        return {"message": "Cart is empty"}
    return checkout(db, current_user.id)
