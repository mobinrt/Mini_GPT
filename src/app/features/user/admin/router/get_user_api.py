from fastapi import Depends, HTTPException, status
from . import router

from src.app.features.user.domain.user_schema import GetUserByID, UserDisplay
from src.app.features.user.domain.user_command import GetUserByIDArgs
from src.app.core.exception.base_exception import BaseError
from src.app.features.user.admin.usecase.get_user_usecase import GetUserUseCase
from src.app.features.user.dependencies import get_user_by_id_usecase

@router.get('/user/by_id/', 
            response_model=UserDisplay, status_code=status.HTTP_200_OK, 
            responses={status.HTTP_404_NOT_FOUND},
            )
async def create_user(id: GetUserByID, get_user_use_case: GetUserUseCase = Depends(get_user_by_id_usecase)):
    try:
        dataclass_instance = GetUserByIDArgs.from_pydantic(id)
        user = await get_user_use_case(dataclass_instance)
        
    except BaseError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
    return user