from fastapi import Depends, HTTPException, status

from . import router
from src.app.features.user.admin.domain.admin_schema import UserDisplayByAdmin
from src.app.features.user.domain.user_schema import GetUserByID
from src.app.features.user.domain.user_command import GetUserByIDArgs
from src.app.core.exception.base_exception import BaseError
from src.app.features.user.admin.usecase.get_user_usecase import GetUserUseCase
from src.app.features.user.dependencies import get_user_by_id_usecase
from src.app.features.user.auth.service.rbac import role_required
from src.app.core.enum.user_role import UserRole
from src.app.features.user.auth.service.auth_service_imp import AuthServiceImp
from src.app.features.user.auth.service.auth_service_imp import oauth2_scheme
from src.app.features.user.dependencies import get_auth_service


@router.get('/user/{id}/', 
            response_model=UserDisplayByAdmin, status_code=status.HTTP_200_OK, 
            responses={status.HTTP_404_NOT_FOUND: {
                        "description": "User not found"    
                    }
                },
            )
@role_required(UserRole.ADMIN.value)  
async def get_user(
    id: int, 
    get_user_use_case: GetUserUseCase = Depends(get_user_by_id_usecase),
    token: str = Depends(oauth2_scheme),
    auth_service : AuthServiceImp = Depends(get_auth_service)  
):
    try:
        role = await auth_service.get_role_from_token(token)
        if role != UserRole.ADMIN.value:
            raise HTTPException(  
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access forbidden: You do not have the required role"
            )

        data = GetUserByID(id=id)
        dataclass_instance = GetUserByIDArgs.from_pydantic(data)
        user = await get_user_use_case(dataclass_instance)

    except BaseError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )

    return user
