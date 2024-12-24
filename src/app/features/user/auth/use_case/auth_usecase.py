from fastapi_jwt_auth import AuthJWT

from src.app.features.user.auth.service.auth_service_imp import AuthServiceImp
from src.app.core.exception.auth_exceptions import InvalidCredentialsError
from src.app.features.user.auth.domain.auth_schemas import TokenDisplay
from src.app.core.utility.hash import verify_password
from src.app.core.enum.user_role import UserRole

class AuthUseCase:
    def __init__(self, auth_service: AuthServiceImp):
        self.auth_service = auth_service

    async def get_token(self, email: str, password: str, Authorize: AuthJWT) -> TokenDisplay:
        user = await self.auth_service.get_user_by_email(email)

        if not user or not verify_password(password, user.password):
            raise InvalidCredentialsError

        role = UserRole(user.role)
        access_token = await self.auth_service.create_access_token(user.id, role, Authorize)
        refresh_token = await self.auth_service.create_refresh_token(user.id, Authorize)

        return TokenDisplay(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type='bearer'
        )

    async def get_dev_token(self, r: str) -> TokenDisplay:
        token = await self.auth_service.create_access_token(user_id="dev_user", role=UserRole(r))
        return TokenDisplay(access_token=token, token_type="bearer")


    async def get_current_user(self, Authorize: AuthJWT):
        return await self.auth_service.get_current_user(Authorize)

    async def refresh_access_token(self, Authorize: AuthJWT) -> TokenDisplay:
        access_token = await self.auth_service.refresh_access_token(Authorize)
        return TokenDisplay(access_token=access_token, token_type='bearer')

    async def get_dev_token(self, r: str) -> TokenDisplay:
        token = await self.auth_service.create_access_token(user_id="dev_user", role=r)
        return TokenDisplay(access_token=token, token_type="bearer")
