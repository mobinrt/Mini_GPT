from abc import abstractmethod, ABC

from src.app.features.user.domain.user_command import CreateUserArgs
from src.app.features.user.repository.user_repo import UserRepository
from src.app.features.user.domain.user_command import CreateUserArgs
from src.app.features.user.domain.user_schema import UserDisplay
from src.app.features.user.domain.model.user_model import UserModel
from src.app.core.utility.imp_uow import IUnitOfWork
from src.app.core.utility.hash import get_password_hash
from src.app.core.abs.abs_usecase import BaseUseCase
from src.app.core.exception.base_exception import BaseError  
   

class CreateUserUseCase(BaseUseCase[CreateUserArgs, UserDisplay], ABC):
    uow: IUnitOfWork
    
    @abstractmethod
    async def __call__(self, args: CreateUserArgs) -> UserDisplay:
        raise NotImplementedError()
    
class ICreateUserUseCase(BaseUseCase[CreateUserArgs, UserDisplay]):
    def __init__(self, uow: IUnitOfWork, execute_method: 'ExecuteCreateUser'):
        self.uow: IUnitOfWork = uow
        self.execute_method = execute_method
        
    async def __call__(self, args: CreateUserArgs) -> UserDisplay: 
        if not args.username:
            raise BaseError(message='Username should not be blank!')
        
        if not args.email:
            raise BaseError(message='Email should not be blank!')
        
        return await self.execute_method.execute(args, self.uow)
        

class ExecuteCreateUser:
    async def execute(self, args: CreateUserArgs, uow: IUnitOfWork) -> UserDisplay:
        async with uow:
            user_repo = uow.get_repository(UserRepository)
            
            existing_user = await user_repo.find_by_email(args.email)
            
            if existing_user:
                raise BaseError(f"This email is already registered.")
            
            hashed_password = get_password_hash(args.password)
            
            new_user = UserModel(
                username=args.username,
                password_hash=hashed_password,
                email=args.email,
            )

            uow.register_model_to_save(new_user)

            user_display = UserDisplay(new_user)

            return user_display