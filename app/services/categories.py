from sqlalchemy.orm import Session
from app.models.categories import Category
from app.schemas.categories import CategoryCreate

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def list_categories(db: Session):
    return db.query(Category).all()