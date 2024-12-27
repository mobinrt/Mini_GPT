from typing import Type, TypeVar, Sequence, Optional
from datetime import datetime
from abc import ABC, abstractmethod

from src.app.core.abs.abs_service import BaseService
from src.app.features.user.domain.model.user_model import UserModel
from src.app.features.user.domain.user_schema import UserDisplay

class UserService(BaseService[UserModel], ABC):
    
    @abstractmethod
    async def find_by_email(self, email: str) -> Optional[UserDisplay]:
        raise NotImplementedError()
    
class IUserService(UserService):
    def __init__(self, model: UserModel):
        self.model = model
    
    async def find_by_email(self, email: str) -> Optional[UserDisplay]:
        user = await self.model.get_or_none(email=email)
        if user: 
            return user 
        return None
