from pydantic import BaseModel

class UserPayload(BaseModel):
    id: int
    email: str
    role: str
