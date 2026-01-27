from fastapi import FastAPI 
from app.routers import users, products, categories, orders, order_item, cart, checkout, payment
from app.config import DATABASE_URL 
app = FastAPI(title="Mi Tienda Completa") 
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
engine = create_engine(DATABASE_URL) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 # Routers 
app.include_router(users.router, prefix="/users", tags=["users"]) 
app.include_router(products.router, prefix="/products", tags=["products"]) 
app.include_router(categories.router, prefix="/categories", tags=["categories"]) 
app.include_router(orders.router, prefix="/orders", tags=["orders"]) 
app.include_router(order_item.router, prefix="/order-items", tags=["order-items"]) 
app.include_router(cart.router, prefix="/cart", tags=["cart"]) 
app.include_router(checkout.router, prefix="/checkout", tags=["checkout"]) 
app.include_router(payment.router, prefix="/payment", tags=["payment"])