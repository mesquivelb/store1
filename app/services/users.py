from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.users import User
from app.schemas.users import UserCreate, UserLogin, Token
from app.auth.auth import (
    get_password_hash,
    verify_password,
    create_access_token,
)
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def login_user(user: UserLogin) -> Token:
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email, "id": user.id}, expires_delta=access_token_expires)
    return Token(
        access_token= access_token,
        token_type= "bearer",
    )

def list_users(db: Session):
    return db.query(User).all()

def get_user_from_payload(db: Session, payload: dict):
    email = payload.get("sub")
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    return user
