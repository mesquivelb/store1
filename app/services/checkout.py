from sqlalchemy.orm import Session
from app.services.cart import list_cart, clear_cart
from app.services.orders import create_order
from app.services.order_item import create_order_item

def checkout_cart(db: Session, user_id: int):
    cart_items = list_cart(db, user_id)
    if not cart_items:
        return None

    total = sum(item.quantity * item.product.price for item in cart_items if hasattr(item, "product"))
    order = create_order(db, {"user_id": user_id, "total": total})

    for item in cart_items:
        create_order_item(db, {"order_id": order.id, "product_id": item.product_id, "quantity": item.quantity, "price": item.quantity * getattr(item.product, "price", 0)})

    clear_cart(db, user_id)
    return order
