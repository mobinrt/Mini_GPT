from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from src.app.features.user.domain.model.user_model import UserModel

_MODEL = TypeVar('_MODEL', bound=UserModel)

class AbstractAuthServices(ABC, Generic[_MODEL]):

    @abstractmethod
    async def get_user_by_email(self, email: str) -> _MODEL | None:
        raise NotImplementedError()

    @abstractmethod
    async def create_access_token(self, user_id: int, role: str) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    async def create_refresh_token(self, user_id: int) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    async def get_current_user(self, token: str) -> _MODEL:
        raise NotImplementedError()

    @abstractmethod
    async def get_role_from_token(self, token: str) -> str:
        raise NotImplementedError()
