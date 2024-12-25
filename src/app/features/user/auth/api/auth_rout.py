from fastapi import APIRouter, status, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT

from ..domain.auth_schemas import TokenDisplay, UserDisplay, LoginRequest
from ..use_case.auth_usecase import AuthUseCase
from ..service.auth_service_imp import AuthServiceImp
from ..dependencies import get_auth_service
from src.app.core.exception.auth_exceptions import InvalidCredentialsError
from src.app.core.exception.base_exception import BaseError
from .rbac import role_required
from src.app.core.enum.user_role import UserRole

router = APIRouter(tags=['authentication'])

@router.post('/token', response_model=TokenDisplay, status_code=status.HTTP_200_OK)
async def login_for_access_token(
    form_data: LoginRequest, 
    Authorize: AuthJWT = Depends(), 
    auth_service: AuthServiceImp = Depends(get_auth_service)
):
    auth_usecase = AuthUseCase(auth_service)

    try:
        return await auth_usecase.get_token(form_data.email, form_data.password, Authorize)
    except InvalidCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid email or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )

@router.post('/refresh-token', response_model=TokenDisplay)
async def refresh_access_token(Authorize: AuthJWT = Depends(), auth_service: AuthServiceImp = Depends(get_auth_service)):
    auth_usecase = AuthUseCase(auth_service)
    
    try:
        return await auth_usecase.refresh_access_token(Authorize)
    except BaseError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid refresh token',
            headers={'WWW-Authenticate': 'Bearer'},
        )

@router.get('/dev-login-token', response_model=TokenDisplay)
async def get_dev_token(auth_service: AuthServiceImp = Depends(get_auth_service)):
    auth_usecase = AuthUseCase(auth_service)
    return await auth_usecase.get_dev_token(role='admin')

@router.get('/read/users/me', response_model=UserDisplay)
async def read_users_me(token: str, auth_service: AuthServiceImp = Depends(get_auth_service)):
    auth_usecase = AuthUseCase(auth_service)
    
    try:
        return await auth_usecase.get_current_user(token)
    except BaseError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid token or user not found',
            headers={'WWW-Authenticate': 'Bearer'},
        )


@router.get("/admin/dashboard")
@role_required(UserRole.ADMIN)
async def admin_dashboard(Authorize: AuthJWT = Depends(), auth_service: AuthServiceImp = Depends(get_auth_service)):
    return {"message": "Welcome to the admin dashboard!"}
