from abc import abstractmethod, ABC

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
    
    
class IGetUserUseCase(BaseUseCase[GetUserByIDArgs, UserDisplay]):
    def __init__(self, uow: IUnitOfWork, execute_method: 'ExecuteGetUser'):
        self.uow: IUnitOfWork = uow
        self.execute_method = execute_method
        
    async def __call__(self, args: GetUserByIDArgs) -> UserDisplay: 
        if args.id < 0:
            raise BaseError('Invalid ID')
        
        return await self.execute_method.execute(args, self.uow)
    
    
class ExecuteGetUser:
    async def execute(self, args: GetUserByIDArgs, uow: IUnitOfWork):
        async with uow.read_only as uow:
            user_repo = uow.get_repository(UserRepository)
            
            existing_user = await user_repo.find_by_id(args.id)
            
            if not existing_user:
                raise BaseError(f"User not found")
            
            user_display = UserDisplay(existing_user)
            return user_display