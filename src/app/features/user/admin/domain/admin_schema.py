from pydantic import BaseModel, Field, model_validator, HttpUrl, EmailStr
from typing import Optional
from datetime import datetime

class UserDisplayByAdmin(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_premium: bool
    image_url: Optional[HttpUrl] = None
    created_at: Optional[datetime] = None 
    updated_at: Optional[datetime] = None 
        
    model_config = {
        'from_attributes': True
    }   
