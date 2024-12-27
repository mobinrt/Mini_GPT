from abc import abstractmethod, ABC
from typing import Type

from src.app.features.user.domain.user_command import GetUserByIDArgs
from src.app.features.user.repository.user_repo import UserRepository 
from src.app.features.user.domain.user_schema import UserDisplay
from src.app.core.utility.imp_uow import IUnitOfWork
from src.app.core.abs.abs_usecase import BaseUseCase
from src.app.core.exception.base_exception import BaseError  
   

class GetUserUseCase(BaseUseCase[GetUserByIDArgs, UserDisplay], ABC):
    uow: IUnitOfWork
    
    @abstractmethod
    async def __call__(self, args: GetUserByIDArgs) -> UserDisplay:
        raise NotImplementedError()
    
    @property
    @abstractmethod
    def execute_method(self):
        raise NotImplementedError()

    
class IGetUserUseCase(BaseUseCase[GetUserByIDArgs, UserDisplay]):
    def __init__(self, uow: IUnitOfWork):
        self.uow: IUnitOfWork = uow
        self._execute_method = ExecuteGetUser()
        
    async def __call__(self, args: GetUserByIDArgs) -> UserDisplay: 
        if args.id < 0:
            raise BaseError('Invalid ID')
        
        return await self.execute_method.execute(args, self.uow)
    
    @property
    def execute_method(self) -> Type['ExecuteGetUser']:
        return self._execute_method
    
class ExecuteGetUser:
    async def execute(self, args: GetUserByIDArgs, uow: IUnitOfWork):
        async with uow.read_only as uow:
            user_repo = uow.get_repository(UserRepository)
            
            existing_user = await user_repo.find_by_id(args.id)
            
            if not existing_user:
                raise BaseError(f"User not found")
            
            user_display = UserDisplay(existing_user)
            return user_display