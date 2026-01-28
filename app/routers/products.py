from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.products import Product, ProductCreate
from app.services.products import create_product, get_product, list_products
from app.database import get_db
from app.auth.services import require_admin
from app.auth.schemas import UserPayload

router = APIRouter()

@router.post("/", response_model=Product)
def add_product(product: ProductCreate, db: Session = Depends(get_db), admin: UserPayload = Depends(require_admin)):
    return create_product(db, product, admin)

@router.get("/", response_model=list[Product])
def all_products(db: Session = Depends(get_db)):
    return list_products(db)

@router.get("/{product_id}", response_model=Product)
def single_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
