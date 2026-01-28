from sqlalchemy.orm import Session
from app.models.products import Product
from app.schemas.products import ProductCreate

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def list_products(db: Session):
    return db.query(Product).all()