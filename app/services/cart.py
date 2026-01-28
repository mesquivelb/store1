from sqlalchemy.orm import Session
from app.models.cart import CartItem
from app.schemas.cart import CartItemCreate

def add_to_cart(db: Session, user_id: int, item : CartItemCreate):
    db_item = CartItem(user_id=user_id,  # seguro, viene del token
        product_id=item.product_id,
        quantity=item.quantity
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def list_cart(db: Session, user_id: int):
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()

def clear_cart(db: Session, user_id: int):
    db.query(CartItem).filter(CartItem.user_id == user_id).delete()
    db.commit()