from sqlalchemy.orm import Session
from app.models.order_item import OrderItem
from app.schemas.order_item import OrderItemCreate
from app.models.products import Product
from fastapi import HTTPException

def create_order_item(db: Session, item: OrderItemCreate, *, price: float):
    product = db.query(Product).filter(Product.id == item.product_id).first()  # ✅ correcto

    if not product:
     raise HTTPException(status_code=404, detail="Product not found")
    
    db_item = OrderItem(
    order_id=item.order_id,
    product_id=item.product_id,
    quantity=item.quantity,
    price=price*item.quantity# aquí ya le pasas directamente item.price
)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def list_order_items(db: Session, order_id: int):
    return db.query(OrderItem).filter(OrderItem.order_id == order_id).all()
