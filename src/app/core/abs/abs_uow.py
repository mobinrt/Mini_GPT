from abc import ABC, abstractmethod
from typing import Type, TypeVar
from tortoise import Model
from contextlib import asynccontextmanager

from .abs_repository import BaseRepository
from .abs_service import BaseService

TRepository = TypeVar('TRepository', bound=BaseRepository)
TService = TypeVar('TService', bound=BaseService)

class AbstractUnitOfWork(ABC):
    
    @abstractmethod
    async def _commit(self):
        raise NotImplementedError()


    @abstractmethod
    async def _rollback(self):
        raise NotImplementedError()

    
    @abstractmethod
    async def __aenter__(self):  
        raise NotImplementedError()
                
    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):  
        raise NotImplementedError()
    
    @asynccontextmanager
    @abstractmethod
    async def read_only(self):
        raise NotImplementedError()
    
    @abstractmethod
    def get_repository(self, repository_in: Type[TRepository]) -> TRepository:
        raise NotImplementedError()
    
    @abstractmethod
    def get_service(self, service_in: Type[TService]) -> TService:
        raise NotImplementedError()
    
    @abstractmethod
    def register_model_to_save(self, model: Model):
        raise NotImplementedError()
