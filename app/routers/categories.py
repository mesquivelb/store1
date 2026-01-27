from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.categories import Category, CategoryCreate
from app.services.categories import create_category, list_categories
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Category)
def add_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)

@router.get("/", response_model=list[Category])
def all_categories(db: Session = Depends(get_db)):
    return list_categories(db)
