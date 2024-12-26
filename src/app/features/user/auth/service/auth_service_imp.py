from fastapi_jwt_auth import AuthJWT
from datetime import timedelta
import jwt

from src.app.core.exception.base_exception import BaseError
from src.app.features.user.domain.model.user_model import UserModel
from src.app.core.abs.abs_auth_services import AbstractAuthServices
from src.app.core.config.setting import settings
from src.app.core.enum.user_role import UserRole


class AuthServiceImp(AbstractAuthServices[UserModel]):
    def __init__(self, model: UserModel):
        self.model = model 

    async def get_user_by_email(self, email: str) -> UserModel | None:
        return await self.model.get_or_none(email=email)

   
    async def create_access_token(self, user_id: int, role: UserRole, Authorize: AuthJWT) -> str:
        expires_delta = timedelta(minutes=settings.access_token_expire_minutes)  
        access_token = Authorize.create_access_token(
            subject=str(user_id),
            user_claims={"role": role.value},
            expires_time=expires_delta,
        )
        return access_token

    async def get_role_from_token(self, Authorize: AuthJWT) -> UserRole:
        try:
            Authorize.jwt_required()
            role = Authorize.get_raw_jwt().get("role")
            if not role:
                raise BaseError("Role not found in token")
            return UserRole(role)
        except jwt.ExpiredSignatureError:
            raise BaseError("Token expired")
        except jwt.InvalidTokenError:
            raise BaseError("Invalid token")


    async def create_refresh_token(self, user_id: int, Authorize: AuthJWT) -> str:
        expires_delta = timedelta(days=settings.refresh_token_expire_days)  
        refresh_token = Authorize.create_refresh_token(
            subject=str(user_id),
            expires_time=expires_delta
        )
        return refresh_token

    async def get_current_user(self, Authorize: AuthJWT) -> UserModel | None:
        try:
            Authorize.jwt_required() 
            user_id = Authorize.get_jwt_subject() 
            role = Authorize.get_raw_jwt().get('role')

            if not user_id or not role:
                raise BaseError('User ID or role missing in token')
            
            user = await self.model.get_or_none(id=user_id)
            if not user:
                raise BaseError('User not found')
            
            return user
        except jwt.ExpiredSignatureError:
            raise BaseError('Token expired')
        except jwt.InvalidTokenError:
            raise BaseError('Invalid token')

    
    async def refresh_access_token(self, Authorize: AuthJWT) -> str:
        try:
            Authorize.jwt_refresh_token_required()
            current_user_id = Authorize.get_jwt_subject()
            new_access_token = Authorize.create_access_token(subject=current_user_id, expires_time=timedelta(minutes=settings.access_token_expire_minutes))
            return new_access_token
        except jwt.ExpiredSignatureError:
            raise BaseError('Refresh token expired')
        except jwt.InvalidTokenError:
            raise BaseError('Invalid refresh token')
