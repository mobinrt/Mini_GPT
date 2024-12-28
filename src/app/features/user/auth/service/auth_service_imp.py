from datetime import timedelta, datetime
from jose import JWTError, jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.app.features.user.domain.model.user_model import UserModel
from src.app.core.config.setting import settings
from src.app.core.enum.user_role import UserRole
from src.app.core.exception.base_exception import BaseError


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class AuthServiceImp:
    def __init__(self):
        self.secret_key = settings.SECRET_KEY
        self.algorithm = settings.ALGORITHM  
        self.access_token_expire_minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES
        self.refresh_token_expire_days = settings.REFRESH_TOKEN_EXPIRE_DAYS

    async def get_user_by_email(self, email: str) -> UserModel | None:
        return await UserModel.get_or_none(email=email)

    async def create_access_token(self, user_id: int, role: UserRole) -> str:
        expires_delta = timedelta(minutes=self.access_token_expire_minutes)
        to_encode = {
            "sub": str(user_id),
            "role": role.value,
            "exp": datetime.now() + expires_delta
        }
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
    
    async def create_refresh_token(self, user_id: int) -> str:
        expires_delta = timedelta(days=self.refresh_token_expire_days)
        to_encode = {
            "sub": str(user_id),
            "exp": datetime.now() + expires_delta
        }
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
    
    
    async def get_current_user(self, token: str = Depends(oauth2_scheme)) -> UserModel:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            user_id: str = payload.get("sub")
            print('user_id: ',user_id)
            if user_id is None:
                raise BaseError('Invalid token')
        except JWTError:
            raise BaseError('Could not validate token')

        user = await UserModel.get_or_none(id=user_id)
        if not user: 
            raise BaseError('User not found')
        return user

    async def get_role_from_token(self, token: str = Depends(oauth2_scheme)) -> UserRole:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            role = payload.get("role")
            if not role:
                raise BaseError("Role not found in token")
            return UserRole(role)
        except JWTError:
            raise BaseError("Could not validate token")
    
    def admin_required(self, user: UserModel = Depends(get_current_user)):
        if not user.is_admin:
            raise BaseError('Admin access required')

    def role_required(self, required_role: UserRole, user: UserModel = Depends(get_current_user)):
        if not user.is_admin and required_role != UserRole.MEMBER:
            raise BaseError('Role not sufficient for this action')
