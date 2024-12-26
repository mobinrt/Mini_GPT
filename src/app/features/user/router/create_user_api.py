from fastapi import Depends, HTTPException, status
from . import router

from src.app.features.user.domain.user_schema import UserCreate, UserDisplay
from src.app.features.user.domain.user_command import CreateUserArgs
from src.app.core.exception.base_exception import BaseError
from src.app.features.user.usecase.create_user_usecase import CreateUserUseCase
from src.app.features.user.dependencies import get_create_user_usecase

@router.post('/create', 
            response_model=UserDisplay, status_code=status.HTTP_201_CREATED, 
            responses={status.HTTP_400_BAD_REQUEST},
            )
async def create_user(user: UserCreate, create_user_use_case: CreateUserUseCase = Depends(get_create_user_usecase)):
    try:
        dataclass_instance = CreateUserArgs.from_pydantic(user)
        new_user = await create_user_use_case(dataclass_instance)
    except BaseError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message
        )
    except Exception as _e:
        print(_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
    return new_user