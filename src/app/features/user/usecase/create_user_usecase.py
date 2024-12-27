from abc import abstractmethod, ABC
from typing import Type

from src.app.features.user.domain.user_command import CreateUserArgs
from src.app.features.user.service.user_service import IUserService, UserService
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

    @property
    @abstractmethod
    def execute_method(self):
        raise NotImplementedError()

class ICreateUserUseCase(BaseUseCase[CreateUserArgs, UserDisplay]):
    def __init__(self, uow: IUnitOfWork):
        self.uow: IUnitOfWork = uow
        self._execute_method = ExecuteCreateUser() 

    async def __call__(self, args: CreateUserArgs) -> UserDisplay: 
        if not args.username:
            raise BaseError('Username should not be blank!')
        
        if not args.email:
            raise BaseError('Email should not be blank!')
        
        return await self._execute_method.execute(args, self.uow)

    @property
    def execute_method(self) -> Type['ExecuteCreateUser']:
        return self._execute_method

class ExecuteCreateUser:
    async def execute(self, args: CreateUserArgs, uow: IUnitOfWork) -> UserDisplay:
       
        async with uow:
            user_service = uow.get_service(IUserService, UserModel)
            existing_user = await user_service.find_by_email(args.email)
            
            if existing_user:
                raise BaseError(f"This email is already registered.")
            
            hashed_password = get_password_hash(args.password)
            
            new_user = UserModel(
                username=args.username,
                password_hash=hashed_password,
                email=args.email,
            )

            uow.register_model_to_save(new_user)
            user_display = UserDisplay.model_validate(new_user)

            return user_display