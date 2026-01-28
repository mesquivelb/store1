from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.config import SECRET_KEY, ALGORITHM
from app.auth.schemas import UserPayload 


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def get_current_user_payload(token: str = Depends(oauth2_scheme))-> UserPayload:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str | None = payload.get("sub")
        user_id: int | None = payload.get("id")
        role: str | None = payload.get("role")
        if email is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
            )
        return UserPayload(id=user_id, email=email, role=role)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    
def require_admin(
    current_user: UserPayload = Depends(get_current_user_payload)
):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin privileges required"
        )
    return current_user
