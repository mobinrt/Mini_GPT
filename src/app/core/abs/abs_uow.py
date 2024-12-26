from abc import ABC, abstractmethod
from typing import Type, TypeVar
from contextlib import asynccontextmanager
from tortoise import Model

from .abs_repository import BaseRepository
from .abs_service import BaseService

TRepository = TypeVar('TRepository', bound=BaseRepository)
TService = TypeVar('TService', bound=BaseService)

class AbstractUnitOfWork(ABC):
    
    @abstractmethod
    async def commit(self):
        raise NotImplementedError()


    @abstractmethod
    async def rollback(self):
        raise NotImplementedError()

    
    @abstractmethod
    @asynccontextmanager
    async def __call__(self):
        raise NotImplementedError()

    @abstractmethod
    @asynccontextmanager
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
