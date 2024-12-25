from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from fastapi_jwt_auth import AuthJWT

from src.app.features.user.domain.model.user_model import UserModel

_MODEL = TypeVar('_MODEL', bound=UserModel)


class AbstractAuthServices(ABC, Generic[_MODEL]):

    @abstractmethod
    async def get_user_by_phone(self, phone: str) -> _MODEL | None:
        raise NotImplementedError()


    @abstractmethod
    async def create_access_token(self, data: dict) -> str:
       raise NotImplementedError()
    
    
    @abstractmethod
    async def create_refresh_token(self, user_id: int, Authorize: AuthJWT) -> str:
        NotImplementedError()
        
        
    @abstractmethod
    async def get_current_user(self, token: str) -> _MODEL:
        raise NotImplementedError()


    @abstractmethod
    async def get_role_from_token(self, token: str) -> str:
        raise NotImplementedError()
    
    async def refresh_access_token(self, Authorize: AuthJWT) -> str:
        raise NotImplementedError()