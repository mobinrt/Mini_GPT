from abc import ABC, abstractmethod
from typing import Dict, Type, TypeVar
from contextlib import asynccontextmanager

from .abc_repository import BaseRepository

TRepository = TypeVar('TRepository', bound=BaseRepository)

class AbstractUnitOfWork(ABC):
    
    @abstractmethod
    @asynccontextmanager
    async def __aenter__(self):
       raise NotImplementedError()


    @abstractmethod
    async def commit(self):
        raise NotImplementedError()


    @abstractmethod
    async def rollback(self):
        raise NotImplementedError()


    @abstractmethod
    async def close(self):
        raise NotImplementedError()


    @abstractmethod
    def get_repository(self, repository_in: Type[TRepository]) -> TRepository:
        raise NotImplementedError()


