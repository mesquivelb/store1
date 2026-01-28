from sqlalchemy.orm import Session
from app.services.cart import list_cart, clear_cart
from app.services.orders import create_order
from app.services.order_item import create_order_item
from app.schemas.order_item import OrderItemCreate
from app.models.cart import CartItem

def checkout_cart(db: Session, user_id: int):
    # Obtener los items del carrito junto con sus productos
    cart_items = (
        db.query(CartItem)
        .filter(CartItem.user_id == user_id)
        .join(CartItem.product)
        .all()
    )

    if not cart_items:
        return None

    # Calcular total de la orden
    total = sum(item.quantity * item.product.price for item in cart_items)

    # Crear la orden
    order_data = {"user_id": user_id, "total": total}
    order = create_order(db, order_data)

    # Crear order items usando Pydantic
    for item in cart_items:
        order_item_data = OrderItemCreate(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
        
        )
        create_order_item(db, order_item_data, price=item.product.price)
    # Vaciar carrito
    clear_cart(db, user_id)

    return order
