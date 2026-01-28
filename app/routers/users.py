from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.users import (
    User,
    UserCreate,
    UserLogin,
    Token,
)
from app.services.users import (
    create_user,
    authenticate_user,
    login_user,
    list_users,
    get_user,
    get_user_by_email,
    get_user_from_payload,
)
from app.auth.services import get_current_user_payload
from app.auth.auth import create_access_token
from app.auth.schemas import UserPayload

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token_data = {"sub": db_user.email, "id": db_user.id, "role": db_user.role}
    token= create_access_token(token_data)
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=User)
def read_users_me(
    current_user: UserPayload = Depends(get_current_user_payload)
):
    return current_user

@router.get("/", response_model=list[User])
def get_users(db: Session = Depends(get_db)):
    return list_users(db)

@router.get("/{user_id}", response_model=User)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
