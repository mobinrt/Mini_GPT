from abc import ABC, abstractmethod
from typing import Type, TypeVar
from contextlib import asynccontextmanager
from tortoise import Model

from .abs_repository import BaseRepository

TRepository = TypeVar('TRepository', bound=BaseRepository)

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
    def get_repository(self, repository_in: Type[TRepository]) -> TRepository:
        raise NotImplementedError()
    
    
    @abstractmethod
    def register_model_to_save(self, model: Model):
        raise NotImplementedError()
