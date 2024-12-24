from pydantic import BaseModel, Field, EmailStr

from src.app.core.enum.user_role import UserRole

class TokenDisplay(BaseModel):
    access_token: str
    token_type: str

    model_config = {
        'from_attributes': True
    }
    
class UserDisplay(BaseModel):
    id: int
    name: str
    role: UserRole 
    
    model_config = {
        'from_attributes': True
    }
    
class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., pattern=r"^0\d{9}$")