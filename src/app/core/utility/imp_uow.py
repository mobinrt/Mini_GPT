from typing import Dict, Type, TypeVar
from contextlib import asynccontextmanager
from tortoise.transactions import in_transaction

from src.app.core.abs.abs_uow import AbstractUnitOfWork
from src.app.core.abs.abs_repository import BaseRepository
from src.app.core.abs.abs_service import BaseService
from src.app.core.config.model.base_model import BaseModel

TRepository = TypeVar('TRepository', bound=BaseRepository)
TService = TypeVar('TService', bound=BaseService)

class IUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.repositories: Dict[str, BaseRepository] = {}
        self.services: Dict[str, BaseService] = {}
        self.models_to_save: list[BaseModel] = [] 

    async def _commit(self):
        for model in self.models_to_save:
            await model.save()  
        self.models_to_save.clear()  


    async def _rollback(self):
        self.models_to_save.clear() 
    
       
    @asynccontextmanager
    async def __call__(self):
        async with in_transaction() as connection:
            try:
                yield self  
                await self._commit 
            except Exception as e:
                await self._rollback()  
                raise e


    @asynccontextmanager
    async def read_only(self):
        yield self


    def get_repository(self, repository_in: Type[TRepository]) -> TRepository:
        if repository_in not in self.repositories:
            self.repositories[repository_in] = repository_in(self)
        return self.repositories[repository_in]


    def get_service(self, service_in: Type[TService]) -> TService:
        if service_in not in self.services:
            self.services[service_in] = service_in(self)
        return self.services[service_in]
    
    
    def register_model_to_save(self, model: BaseModel):
        self.models_to_save.append(model)
