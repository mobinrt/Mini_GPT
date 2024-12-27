from fastapi import Depends

from src.app.features.user.repository.user_repo import UserRepository
from src.app.features.user.domain.model.user_model import UserModel
from src.app.features.user.service.user_service import UserService, IUserService
from src.app.core.abs.abs_repository import BaseRepository
from src.app.core.abs.abs_auth_services import AbstractAuthServices
from src.app.core.abs.abs_uow import AbstractUnitOfWork
from src.app.features.user.auth.service.auth_service_imp import AuthServiceImp
from src.app.core.utility.imp_uow import IUnitOfWork
from src.app.features.user.usecase.create_user_usecase import CreateUserUseCase, ICreateUserUseCase
from src.app.features.user.admin.usecase.get_user_usecase import GetUserUseCase, IGetUserUseCase


async def get_user_repository() -> BaseRepository:
    return UserRepository()


async def get_user_service(model: UserModel = Depends()) -> UserService:
    return IUserService(model)


async def get_auth_service() -> AbstractAuthServices:
    return AuthServiceImp()

async def get_user_unit_of_work() -> AbstractUnitOfWork:
    return IUnitOfWork()


async def get_create_user_usecase(
    uow: IUnitOfWork = Depends(get_user_unit_of_work),
    # user_service: IUserService = Depends(get_user_service)
) -> CreateUserUseCase:
    return ICreateUserUseCase(uow)


async def get_user_by_id_usecase(
    uow: IUnitOfWork = Depends(get_user_unit_of_work)
    ) -> GetUserUseCase:
     return IGetUserUseCase(uow)


# async def get_users_use_case(uow: IUnitOfWork = Depends(get_user_unit_of_work)) -> GetUsersUseCase:
#     return GetUsersUseCaseImp(uow)
 
 
# async def get_delete_user_use_case(
#     unit_of_work: IUnitOfWork = Depends(get_user_unit_of_work),
# ) -> DeleteUserUseCase:
#     return DeleteUserUseCaseImpl(unit_of_work)



# async def get_update_user_use_case(
#     unit_of_work: IUnitOfWork = Depends(get_user_unit_of_work),
#     auth: UserAuthService = Depends(get_auth_service),
# ) -> UpdateUserUseCase:
#     return UpdateUserUseCaseImp(unit_of_work, auth)
